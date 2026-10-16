import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.db import Base, get_db
from app.main import app
from app.models import RequestEvent


@pytest.fixture
def client():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    def test_db():
        with Session(engine) as session:
            yield session
    app.dependency_overrides[get_db] = test_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    engine.dispose()


def report(client, **changes):
    data = {"title": "Library lamp flickers", "location": "Library desk 12",
            "category": "ELECTRICAL", "reporter": "Rudray Mehra", "urgency": "URGENT"}
    data.update(changes)
    response = client.post("/api/requests", json=data)
    assert response.status_code == 201, response.text
    return response.json()


def test_health_and_identity(client):
    assert client.get("/health").json() == {"status": "UP"}
    assert client.get("/").json()["service"] == "CampusFix API"
    assert client.get("/ready").status_code == 200


def test_create_read_and_list(client):
    item = report(client)
    assert item["status"] == "REPORTED"
    assert item["resolution"] == ""
    assert client.get("/api/requests/" + str(item["id"])).json() == item
    assert client.get("/api/requests").json() == [item]


def test_filter_by_status_category_and_location(client):
    report(client)
    second = report(client, title="Tap leaking", category="PLUMBING", location="Hostel B")
    client.put("/api/requests/" + str(second["id"]), json={"status": "IN_PROGRESS"})
    assert len(client.get("/api/requests?status=REPORTED").json()) == 1
    assert client.get("/api/requests?category=PLUMBING").json()[0]["id"] == second["id"]
    assert client.get("/api/requests?q=hostel").json()[0]["id"] == second["id"]
    assert client.get("/api/requests?q=%25").json() == []
    assert client.get("/api/requests?status=INVALID").status_code == 422


def test_resolution_and_reopening(client):
    item = report(client)
    url = "/api/requests/" + str(item["id"])
    assert client.put(url, json={"status": "RESOLVED", "resolution": "Replaced bulb"}).status_code == 409
    assert client.put(url, json={"status": "IN_PROGRESS"}).status_code == 200
    assert client.put(url, json={"status": "RESOLVED"}).status_code == 422
    assert client.put(url, json={"status": "RESOLVED", "resolution": "  "}).status_code == 422
    result = client.put(url, json={"status": "RESOLVED", "resolution": "Replaced bulb; checked lighting"}).json()
    assert result["status"] == "RESOLVED"
    assert client.get("/api/requests/stats").json()["urgentOpen"] == 0
    reopened = client.put(url, json={"status": "REPORTED"}).json()
    assert reopened["resolution"] == ""
    assert reopened["status"] == "REPORTED"


def test_resolution_cannot_be_set_on_open_request(client):
    item = report(client)
    assert client.put("/api/requests/" + str(item["id"]), json={"resolution": "Fixed"}).status_code == 422


def test_edit_records_real_activity(client):
    item = report(client)
    url = "/api/requests/" + str(item["id"])
    response = client.put(url, json={"location": "Library desk 13", "urgency": "NORMAL"})
    assert response.status_code == 200
    assert response.json()["location"] == "Library desk 13"
    events = client.get("/api/activity").json()
    assert len(events) == 2
    assert "location" in events[0]["message"]
    assert events[0]["request_id"] == item["id"]
    client.put(url, json={"location": "Library desk 13"})
    assert len(client.get("/api/activity").json()) == 2  # no fabricated activity for no-op updates


@pytest.mark.parametrize("body", [{"title": None}, {"status": None}, {"urgency": "EXTREME"}, {"location": " "}])
def test_invalid_updates_do_not_change_data(client, body):
    item = report(client)
    url = "/api/requests/" + str(item["id"])
    assert client.put(url, json=body).status_code == 422
    assert client.get(url).json() == item


@pytest.mark.parametrize("field,value", [("title", " "), ("location", ""), ("reporter", ""), ("category", "UNKNOWN"), ("urgency", "HIGH")])
def test_invalid_reports(client, field, value):
    payload = {"title": "Chair leg loose", "location": "Lab 1", "reporter": "Rudray", "category": "FURNITURE"}
    payload[field] = value
    assert client.post("/api/requests", json=payload).status_code == 422


def test_whitespace_trimmed(client):
    assert report(client, title="  Broken library lamp  ")["title"] == "Broken library lamp"


def test_delete_removes_related_activity(client):
    item = report(client)
    url = "/api/requests/" + str(item["id"])
    assert client.delete(url).status_code == 204
    assert client.get(url).status_code == 404
    assert client.get("/api/activity").json() == []
    assert client.get("/api/requests/stats").json()["total"] == 0


@pytest.mark.parametrize("method", ["get", "put", "delete"])
def test_missing_request(client, method):
    response = getattr(client, method)("/api/requests/9999", **({"json": {"status": "IN_PROGRESS"}} if method == "put" else {}))
    assert response.status_code == 404


def test_stats(client):
    report(client)
    item = report(client, urgency="NORMAL", category="NETWORK")
    client.put("/api/requests/" + str(item["id"]), json={"status": "IN_PROGRESS"})
    assert client.get("/api/requests/stats").json() == {"total": 2, "reported": 1, "inProgress": 1, "resolved": 0, "urgentOpen": 1}


def test_readiness_failure_keeps_liveness(client):
    class UnavailableDatabase:
        def execute(self, _):
            raise OperationalError("SELECT", {}, Exception("unavailable"))
    app.dependency_overrides[get_db] = lambda: UnavailableDatabase()
    assert client.get("/ready").status_code == 503
    assert client.get("/health").status_code == 200


def test_metrics_include_requests(client):
    client.get("/health")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text


def test_activity_limit(client):
    report(client)
    report(client, title="Lab socket broken")
    assert len(client.get("/api/activity?limit=1").json()) == 1
    assert client.get("/api/activity?limit=0").status_code == 422
