"""Capture live monitoring/GitOps browser evidence and assert Prometheus data."""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import expect, sync_playwright

output = Path("session21-python/evidence/observability")
output.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1440, "height": 1000})
    page = context.new_page()
    response = context.request.get("http://127.0.0.1:9090/api/v1/targets").json()
    targets = [t for t in response["data"]["activeTargets"] if t["labels"].get("namespace") == "taskboard"]
    assert len(targets) >= 2 and all(t["health"] == "up" for t in targets)
    queries = {}
    for name, query in {
        "request_rate": 'sum(rate(http_requests_total{namespace="taskboard"}[5m]))',
        "latency_p95": 'histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{namespace="taskboard"}[5m])) by (le))',
    }.items():
        data = context.request.get("http://127.0.0.1:9090/api/v1/query", params={"query": query}).json()
        assert data["status"] == "success" and data["data"]["result"], data
        queries[name] = data
    page.goto("http://127.0.0.1:9090/targets")
    expect(page.get_by_text("serviceMonitor/taskboard/taskboard-backend/0", exact=False).first).to_be_visible(timeout=30000)
    page.screenshot(path=str(output / "prometheus-targets.png"), full_page=True)
    page.goto("http://127.0.0.1:3100/login")
    page.get_by_label("Email or username").fill("admin")
    page.get_by_label("Password", exact=True).fill("campusfix-local-demo")
    page.get_by_role("button", name="Log in", exact=True).click()
    page.wait_for_timeout(2000)
    page.goto("http://127.0.0.1:3100/d/campusfix-app/campusfix-application?from=now-15m&to=now")
    expect(page.get_by_text("Request latency p95", exact=True)).to_be_visible(timeout=30000)
    page.wait_for_timeout(4000)
    page.screenshot(path=str(output / "grafana-dashboard.png"), full_page=True)

    password = subprocess.check_output(["kubectl", "--context", "campusfix-eks", "-n", "argocd",
        "get", "secret", "argocd-initial-admin-secret", "-o", "jsonpath={.data.password}"], text=True)
    import base64
    page.goto("http://127.0.0.1:8089/")
    page.locator('input[name="username"]').fill("admin")
    page.locator('input[name="password"]').fill(base64.b64decode(password).decode())
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(2000)
    page.goto("http://127.0.0.1:8089/applications/argocd/campusfix?view=tree")
    expect(page.get_by_text("Healthy", exact=True).first).to_be_visible(timeout=30000)
    expect(page.get_by_text("Synced", exact=True).first).to_be_visible(timeout=30000)
    page.screenshot(path=str(output / "argocd-synced.png"), full_page=True)
    (output / "result.json").write_text(json.dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "passed", "targets": targets, "queries": queries,
        "argocd": "Synced and Healthy shown in live UI",
    }, indent=2) + "\n")
    print("PASS: Prometheus targets and queries, Grafana dashboard, Argo CD live screenshots.")
    browser.close()
