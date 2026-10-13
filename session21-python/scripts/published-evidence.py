"""Capture public CI/package pages and a clearly labelled view of actual pytest output."""
import html
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

output = Path("session21-python/evidence/published")
output.mkdir(parents=True, exist_ok=True)
runs = {"foundation": 38372002674, "session16": 38341620592, "session17": 38342666869, "campusfix": 38342666849}
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1440, "height": 1050})
    page = context.new_page()
    results = {}
    for name, run_id in runs.items():
        api_url = f"https://api.github.com/repos/rudraymehra/devops-heros/actions/runs/{run_id}"
        data = context.request.get(api_url).json()
        assert data["conclusion"] == "success", data
        results[name] = {k: data[k] for k in ["id", "name", "head_sha", "html_url", "conclusion", "updated_at"]}
        page.goto(data["html_url"], wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2000)
        page.screenshot(path=str(output / (name + "-ci.png")))
    for name, url in {
        "commits": "https://github.com/rudraymehra/devops-heros/commits/main/",
        "backend-package": "https://github.com/users/rudraymehra/packages/container/package/campusfix-backend",
        "frontend-package": "https://github.com/users/rudraymehra/packages/container/package/campusfix-frontend",
    }.items():
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(1500)
        page.screenshot(path=str(output / (name + ".png")))
    log = Path("session21-python/evidence/pytest.md").read_text()
    page.set_content("<html><style>body{font:16px monospace;padding:24px;background:#101b2e;color:#eaf0fa}pre{white-space:pre-wrap}</style>"
                     "<h2>Actual pytest command evidence</h2><p>Rendered log view, not a native terminal screenshot.</p><pre>"
                     + html.escape(log) + "</pre></html>")
    page.screenshot(path=str(output / "pytest-log-view.png"), full_page=True)
    (output / "ci-runs.json").write_text(json.dumps(results, indent=2) + "\n")
    print("PASS: four successful public CI runs verified and pages captured.")
    browser.close()
