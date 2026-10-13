"""Exercise the real app and capture desktop/mobile evidence; requires Playwright."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import expect, sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://127.0.0.1:3000")
parser.add_argument("--output", default="session21-python/evidence/browser")
args = parser.parse_args()
output = Path(args.output)
output.mkdir(parents=True, exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    context = browser.new_context(viewport={"width": 1440, "height": 1080},
                                  record_video_dir=str(output / "video"),
                                  record_video_size={"width": 1440, "height": 1080})
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    existing = context.request.get(args.url + "/api/requests").json()
    samples = [
        ("Reading lamp flickers near the window", "Library · Floor 2, desk 12", "ELECTRICAL", "URGENT", "Light flickers after a few minutes of use. Please check the fixture."),
        ("Wi-Fi drops during practical sessions", "Computer lab · Room 204", "NETWORK", "NORMAL", "The connection drops at the back row. Reconnecting helps briefly."),
        ("Drinking water tap keeps leaking", "Academic block · Ground floor", "PLUMBING", "URGENT", "Water continues to drip when the handle is fully closed."),
        ("Loose chair leg in the study area", "Student centre · Study room", "FURNITURE", "NORMAL", "One leg is unstable. The chair has been moved aside."),
    ]
    for index, (title, location, category, urgency, description) in enumerate(samples):
        if any(item["title"] == title for item in existing):
            continue
        response = context.request.post(args.url + "/api/requests", data={
            "title": title, "location": location, "category": category,
            "urgency": urgency, "description": description, "reporter": "Sudhir Mehra",
        })
        assert response.status == 201, response.text()
        item_id = response.json()["id"]
        if index in (1, 3):
            assert context.request.put(args.url + "/api/requests/" + str(item_id), data={"status": "IN_PROGRESS"}).ok
        if index == 3:
            assert context.request.put(args.url + "/api/requests/" + str(item_id), data={
                "status": "RESOLVED", "resolution": "Tightened the leg fittings and checked stability.",
            }).ok

    page.goto(args.url)
    expect(page.get_by_role("heading", name="Let’s get it fixed.")).to_be_visible()
    expect(page.get_by_role("button", name=samples[0][0], exact=True)).to_be_visible()
    page.screenshot(path=str(output / "desktop.png"), full_page=True)

    title = "Browser verification: library socket"
    page.get_by_role("button", name="Report an issue").click()
    page.get_by_label("Issue title", exact=True).fill(title)
    page.get_by_label("Location", exact=True).fill("Library desk 28")
    page.get_by_label("Description", exact=True).fill("Verification request created through the browser.")
    page.get_by_label("Urgency", exact=True).select_option("URGENT")
    page.get_by_role("button", name="Save request", exact=True).click()
    expect(page.get_by_role("dialog")).to_have_count(0)
    expect(page.get_by_role("button", name=title, exact=True)).to_be_visible()
    page.get_by_role("button", name=title, exact=True).click()
    page.get_by_role("button", name="Start work", exact=True).click()
    expect(page.get_by_role("dialog")).to_have_count(0)
    page.get_by_role("button", name=title, exact=True).click()
    page.get_by_label("Resolution notes", exact=True).fill("Replaced the socket cover and tested power.")
    page.screenshot(path=str(output / "resolution-form.png"), full_page=True)
    page.get_by_role("button", name="Mark resolved", exact=True).click()
    expect(page.get_by_role("dialog")).to_have_count(0)
    page.get_by_role("button", name=title, exact=True).click()
    expect(page.get_by_text("Replaced the socket cover and tested power.", exact=True)).to_be_visible()
    page.get_by_role("button", name="Reopen request", exact=True).click()
    expect(page.get_by_role("dialog")).to_have_count(0)
    page.get_by_role("button", name=title, exact=True).click()
    page.get_by_role("button", name="Edit details", exact=True).click()
    page.get_by_label("Location", exact=True).fill("Library desk 29")
    page.get_by_role("button", name="Save request", exact=True).click()
    expect(page.get_by_role("dialog")).to_have_count(0)
    expect(page.get_by_text("⌖ Library desk 29", exact=True)).to_be_visible()
    page.get_by_label("Search requests", exact=True).fill("Library desk 29")
    expect(page.locator(".request-card")).to_have_count(1)
    page.get_by_label("Search requests", exact=True).fill("")

    # A failed save must preserve the entered text and show a real error.
    page.get_by_role("button", name="Report an issue").click()
    page.get_by_label("Issue title", exact=True).fill("Unsaved issue should remain")
    page.get_by_label("Location", exact=True).fill("Lab 2")
    def fail_save(route):
        if route.request.method == "POST":
            route.fulfill(status=503, json={"detail": "Temporary maintenance"})
        else:
            route.continue_()
    page.route("**/api/requests", fail_save)
    page.get_by_role("button", name="Save request", exact=True).click()
    expect(page.get_by_role("alert")).to_contain_text("Temporary maintenance")
    expect(page.get_by_label("Issue title", exact=True)).to_have_value("Unsaved issue should remain")
    page.unroute("**/api/requests", fail_save)
    page.get_by_role("button", name="Close dialog", exact=True).click()

    page.get_by_role("button", name=title, exact=True).click()
    page.get_by_role("button", name="Delete request", exact=True).click()
    page.get_by_role("button", name="Delete permanently", exact=True).click()
    expect(page.get_by_role("dialog")).to_have_count(0)
    expect(page.get_by_role("button", name=title, exact=True)).to_have_count(0)

    page.set_viewport_size({"width": 390, "height": 844})
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"), "Mobile page overflows"
    page.screenshot(path=str(output / "mobile.png"), full_page=True)
    video = page.video
    context.close()
    video.save_as(str(output / "browser-walkthrough.webm"))
    browser.close()
    assert not errors, errors
    result = {"status": "passed", "timestamp": datetime.now(timezone.utc).isoformat(), "url": args.url,
              "checks": ["create", "start work", "resolve with notes", "reopen", "edit",
                         "search", "failed-save draft retention", "delete", "mobile layout"],
              "browser_errors": errors, "sample_data": "Four synthetic campus maintenance reports"}
    (output / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
