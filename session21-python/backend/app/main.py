from fastapi import Depends, FastAPI, HTTPException, Query, status
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy import func, or_, select, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .config import settings
from .db import get_db
from .models import MaintenanceRequest, RequestEvent, utc_now
from .schemas import Category, EventOut, RequestCreate, RequestOut, RequestStatus, RequestUpdate

app = FastAPI(title=settings.app_name, version="2.0.0")
Instrumentator().instrument(app).expose(app, endpoint="/metrics")


def find_request(db: Session, request_id: int):
    item = db.get(MaintenanceRequest, request_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Maintenance request not found")
    return item


@app.get("/")
def root():
    return {"service": settings.app_name, "version": "2.0.0", "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/ready")
def ready(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1 FROM maintenance_requests LIMIT 1"))
    except SQLAlchemyError as exc:
        raise HTTPException(status_code=503, detail="Database is not ready") from exc
    return {"status": "READY"}


@app.get("/api/requests", response_model=list[RequestOut])
def list_requests(
    status: RequestStatus | None = None,
    category: Category | None = None,
    q: str = Query(default="", max_length=200),
    db: Session = Depends(get_db),
):
    query = select(MaintenanceRequest)
    if status:
        query = query.where(MaintenanceRequest.status == status)
    if category:
        query = query.where(MaintenanceRequest.category == category)
    if q.strip():
        query = query.where(or_(
            MaintenanceRequest.title.icontains(q.strip(), autoescape=True),
            MaintenanceRequest.location.icontains(q.strip(), autoescape=True),
        ))
    return list(db.scalars(query.order_by(MaintenanceRequest.id.desc())))


@app.get("/api/requests/stats")
def stats(db: Session = Depends(get_db)):
    rows = db.execute(select(MaintenanceRequest.status, func.count())
                      .group_by(MaintenanceRequest.status)).all()
    counts = dict(rows)
    urgent = db.scalar(select(func.count()).select_from(MaintenanceRequest).where(
        MaintenanceRequest.urgency == "URGENT", MaintenanceRequest.status != "RESOLVED"))
    return {"total": sum(counts.values()), "reported": counts.get("REPORTED", 0),
            "inProgress": counts.get("IN_PROGRESS", 0), "resolved": counts.get("RESOLVED", 0),
            "urgentOpen": urgent}


@app.get("/api/activity", response_model=list[EventOut])
def activity(limit: int = Query(default=8, ge=1, le=50), db: Session = Depends(get_db)):
    return list(db.scalars(select(RequestEvent).order_by(RequestEvent.id.desc()).limit(limit)))


@app.get("/api/requests/{request_id}", response_model=RequestOut)
def get_request(request_id: int, db: Session = Depends(get_db)):
    return find_request(db, request_id)


@app.post("/api/requests", response_model=RequestOut, status_code=status.HTTP_201_CREATED)
def create_request(payload: RequestCreate, db: Session = Depends(get_db)):
    item = MaintenanceRequest(**payload.model_dump())
    item.events.append(RequestEvent(message=f"Reported: {payload.title}"))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.put("/api/requests/{request_id}", response_model=RequestOut)
def update_request(request_id: int, payload: RequestUpdate, db: Session = Depends(get_db)):
    item = find_request(db, request_id)
    changes = payload.model_dump(exclude_unset=True)
    next_status = changes.get("status", item.status)
    allowed = {"REPORTED": {"REPORTED", "IN_PROGRESS"},
               "IN_PROGRESS": {"IN_PROGRESS", "RESOLVED"}, "RESOLVED": {"RESOLVED", "REPORTED"}}
    if next_status not in allowed[item.status]:
        raise HTTPException(status_code=409, detail="Start work before resolving a request")
    resolution = changes.get("resolution", item.resolution)
    if next_status == "RESOLVED" and not resolution.strip():
        raise HTTPException(status_code=422, detail="Resolution notes are required")
    if next_status != "RESOLVED" and changes.get("resolution", "").strip():
        raise HTTPException(status_code=422, detail="Resolution notes belong to a resolved request")
    if item.status == "RESOLVED" and next_status == "REPORTED":
        changes["resolution"] = ""
    changed_fields = [key for key, value in changes.items() if getattr(item, key) != value]
    if changed_fields:
        if item.status != next_status:
            message = f"{item.status.replace('_', ' ').title()} → {next_status.replace('_', ' ').title()}: {item.title}"
        else:
            message = f"Updated {', '.join(changed_fields)}: {item.title}"
        for key, value in changes.items():
            setattr(item, key, value)
        item.updated_at = utc_now()
        item.events.append(RequestEvent(message=message[:250]))
        db.commit()
        db.refresh(item)
    return item


@app.delete("/api/requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_request(request_id: int, db: Session = Depends(get_db)):
    db.delete(find_request(db, request_id))
    db.commit()
