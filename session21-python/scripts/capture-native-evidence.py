"""Run real capstone checks; optionally capture user-selected macOS windows.

No screenshot rendering, cloud creation/deletion, Git writes, or volume deletion.
Run with --help for the opt-in Compose and Kubernetes checks.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import signal
import subprocess
import sys
from datetime import datetime, timezone


PROJECT = Path(__file__).resolve().parents[1]
IDENTITY = "Rudray Mehra | 24 BCS 10425 | Batch B"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def executable(name, fallback=None):
    return shutil.which(name) or (str(fallback) if fallback and Path(fallback).is_file() else name)


def execute(command, cwd, timeout):
    """Bound the whole command process group, including child processes."""
    try:
        process = subprocess.Popen(
            command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, errors="replace", start_new_session=True,
            env={**os.environ, "NO_COLOR": "1", "TERM": "dumb"},
        )
    except OSError as error:
        return 127, str(error) + "\n"
    try:
        output, _ = process.communicate(timeout=timeout)
        code = process.returncode
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        output, _ = process.communicate()
        output += f"\nSTOPPED: command exceeded {timeout} seconds. No success claimed.\n"
        code = 124
    # Account numbers and ANSI controls are not needed in submission logs.
    output = re.sub(r"\b\d{12}\b", "[AWS_ACCOUNT_ID]", output)
    output = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", output)
    return code, output


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def execution_succeeded(code, output):
    # Some macOS diagnostics return zero even when sysctl/socket access is denied.
    return code == 0 and not re.search(r"operation not permitted|permission denied", output, re.IGNORECASE)


def capture_window(path, description):
    print(f"\nCapture: {description}")
    print("Select ONLY the relevant Terminal/browser window, with no private information.")
    print("For Terminal, keep the command, result and Rudray Mehra heading visible.")
    if input("Enter = select window; s = skip this screenshot: ").strip().lower() == "s":
        return None
    result = subprocess.run(["/usr/sbin/screencapture", "-i", "-w", "-o", "-x", str(path)])
    if result.returncode or not path.is_file() or not path.read_bytes().startswith(PNG_SIGNATURE):
        print("Screenshot was cancelled or macOS denied capture; NOT marked captured.")
        return None
    print(f"Saved untouched native screenshot: {path}")
    return {"file": path.name, "sha256": file_hash(path),
            "type": "native macOS window capture; selected by user; visual review required"}


class EvidenceRun:
    def __init__(self, output, screenshots=False):
        self.output = output
        output.mkdir(parents=True, exist_ok=False)
        self.screenshots = screenshots
        self.records = []

    def save(self):
        manifest = {"student": IDENTITY, "records": self.records}
        (self.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        lines = ["# Fresh command evidence", "", IDENTITY, "",
                 "These commands were actually executed. Logs are not screenshots.",
                 "Native images, if present, are untouched user-selected macOS window captures.",
                 "Check each image visually before submission; file creation alone does not prove its contents.",
                 "", "| Check | Execution | Log | Native screenshot |",
                 "|---|---|---|---|"]
        for item in self.records:
            shot = item.get("screenshot")
            shot_link = f"[Review image]({shot['file']})" if shot else "NOT CAPTURED"
            log = f"[Output]({item['log']})" if item.get("log") else "—"
            lines.append(f"| {item['title']} | {item['status']} | {log} | {shot_link} |")
        lines += ["", "An exit code of zero proves only the named command succeeded.",
                  "Helm lint is not a deployment; Terraform validate is not a plan/apply/destroy.",
                  "No AWS resources were created or removed by this helper.", ""]
        (self.output / "README.md").write_text("\n".join(lines))

    def check(self, slug, title, command, cwd=PROJECT, timeout=120):
        if self.screenshots:
            print("\033[2J\033[H", end="", flush=True)
        started = datetime.now(timezone.utc).isoformat()
        heading = f"{IDENTITY}\n{title}\nUTC: {started}\nDirectory: {cwd}\nCommand: {shlex.join(command)}\n"
        print(heading, flush=True)
        print(f"Running (maximum {timeout}s); complete output will appear below.\n", flush=True)
        code, output = execute(command, cwd, timeout)
        passed = execution_succeeded(code, output)
        print(output, end="" if output.endswith("\n") else "\n")
        result = f"Exit code: {code} | {'PASSED' if passed else 'FAILED / BLOCKED'} | {IDENTITY}\n"
        if code == 0 and not passed:
            result += "Assessment: command reported a permission error despite exit 0; not accepted as successful evidence.\n"
        print(result, flush=True)
        logfile = self.output / f"{slug}.txt"
        logfile.write_text(heading + "\n" + output + "\n" + result)
        record = {"title": title, "status": "PASS" if passed else "FAILED / BLOCKED",
                  "command": command, "cwd": str(cwd), "timestamp": started, "exit_code": code,
                  "log": logfile.name, "log_sha256": file_hash(logfile), "screenshot": None}
        self.records.append(record)
        self.save()
        if self.screenshots:
            record["screenshot"] = capture_window(self.output / f"{slug}.png", title)
            self.save()
        return passed

    def skip(self, title, reason):
        print(f"NOT RUN: {title}: {reason}", flush=True)
        self.records.append({"title": title, "status": "NOT RUN: " + reason})
        self.save()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screenshots", action="store_true", help="Interactively select each native Mac window")
    parser.add_argument("--compose", action="store_true", help="Build/start only the local campusfix Compose project; keep volumes")
    parser.add_argument("--kube-context", help="Read-only checks against an explicitly chosen existing cluster")
    parser.add_argument("--terraform", help="Path to Terraform; validates without creating cloud resources")
    parser.add_argument("--terraform-plan", action="store_true", help="Also run a real AWS plan (read-only; needs AWS login); NEVER apply")
    parser.add_argument("--output", type=Path, help="New output directory; must not already exist")
    args = parser.parse_args()
    if args.screenshots and (sys.platform != "darwin" or not sys.stdin.isatty()):
        parser.error("--screenshots requires an interactive macOS Terminal; omit it for logs only")
    output = args.output or PROJECT / "evidence" / "terminal" / datetime.now().strftime("rudray-%Y%m%d-%H%M%S-%f")
    run = EvidenceRun(output.resolve(), args.screenshots)
    print("CampusFix evidence collection. No AWS changes, no pruning, no Git push.")
    if args.compose:
        print("Compose will build/recreate this lab's app containers and run pending migrations; existing database volume is kept.")
        print("The local stack remains running for your browser/demo. Stop later with docker compose -p campusfix down.")
    python = str(PROJECT / "backend" / ".venv" / "bin" / "python")
    run.check("01-pytest", "M2 — actual isolated API tests", [python, "-m", "pytest", "-v"], PROJECT / "backend")
    run.check("02-frontend-build", "M1/M5 — React production build", [executable("npm"), "run", "build"], PROJECT / "frontend")
    run.check("03-helm-lint", "M8 — Helm syntax check (not deployment)", [executable("helm"), "lint", "helm/taskboard"])
    terraform = args.terraform or shutil.which("terraform")
    if terraform:
        valid = run.check("04-terraform-validate", "M7 — Terraform validation (not cloud execution)",
                          [terraform, "validate", "-no-color"], PROJECT / "terraform", timeout=60)
        if args.terraform_plan and valid:
            run.check("04b-terraform-plan", "M7 — actual read-only AWS plan (no apply)",
                      [terraform, "plan", "-input=false", "-no-color", "-lock-timeout=15s"],
                      PROJECT / "terraform", timeout=180)
        else:
            run.skip("M7 — new Terraform plan", "Not requested or validation failed; historical plan remains separate")
    else:
        run.skip("M7 — Terraform validation/plan", "Terraform not on PATH; supply --terraform /path/to/terraform")

    if args.compose:
        docker = executable("docker", "/Applications/Docker.app/Contents/Resources/bin/docker")
        compose = [docker, "compose", "-p", "campusfix"]
        engine_ok = run.check("05-docker-engine", "M4 — Docker client and server", [docker, "version"], timeout=20)
        if engine_ok:
            up = run.check("06-compose-start", "M4 — build and start frontend/backend/PostgreSQL",
                           compose + ["up", "--build", "-d", "--wait", "--wait-timeout", "180"], timeout=900)
            run.check("07-compose-status", "M4 — actual Compose service status", compose + ["ps", "--all"], timeout=30)
            if up:
                for service in ("backend", "frontend"):
                    run.check(f"08-nonroot-{service}", f"M4 — {service} non-root UID (must not be 0)",
                              compose + ["exec", "-T", service, "sh", "-c", 'id; test "$(id -u)" -ne 0'], timeout=30)
                run.check("09-alembic", "M1 — migration revision in real PostgreSQL stack",
                          compose + ["exec", "-T", "backend", "alembic", "current"], timeout=30)
                curl = [executable("curl"), "--fail", "--silent", "--show-error", "--max-time", "15"]
                run.check("10-health", "M1 — live FastAPI health", curl + ["http://localhost:8000/health"], timeout=20)
                run.check("11-ready", "M1 — real database/schema readiness", curl + ["http://localhost:8000/ready"], timeout=20)
                run.check("12-api", "M1 — live maintenance REST API", curl + ["http://localhost:8000/api/requests/stats"], timeout=20)
                run.check("13-metrics", "M9 — live Prometheus metrics (not evidence of a cluster scrape)",
                          curl + ["http://localhost:8000/metrics"], timeout=20)
                if args.screenshots:
                    subprocess.run(["/usr/bin/open", "http://localhost:3000"], check=False)
                    print("In the browser, verify CampusFix loads and the profile says Rudray Mehra.")
                    print("Do not change or relabel historic database records for a screenshot.")
                    shot = capture_window(run.output / "14-localhost-browser.png", "M1/M4 — localhost:3000 application")
                    run.records.append({"title": "M1/M4 — localhost browser", "status": "VISUAL REVIEW REQUIRED",
                                        "screenshot": shot})
                    run.save()
            else:
                run.skip("Live API/browser", "Compose startup failed; inspect the captured error before retrying")
        else:
            run.skip("Compose/live API/browser", "Docker server unavailable; open/restart Docker Desktop, then retry")
    else:
        run.skip("Compose/live API/browser", "Not requested; add --compose to run this local lab")

    if args.kube_context:
        kubectl = [executable("kubectl"), "--context", args.kube_context, "--request-timeout=15s", "-n", "taskboard"]
        for resource in ("pods", "deployments", "svc", "ingress"):
            run.check("15-k8s-" + resource, "M8 — actual Kubernetes " + resource,
                      kubectl + ["get", resource, "-o", "wide"], timeout=30)
        run.check("16-helm-list", "M8 — actual Helm releases",
                  [executable("helm"), "list", "--kube-context", args.kube_context, "-n", "taskboard"], timeout=30)
        print("Review output: get/list exit 0 alone does not prove all Pods Running, two ready app replicas, or a deployed release.")
    else:
        run.skip("Kubernetes/Helm deployment", "No explicit --kube-context supplied; the earlier AWS lab was destroyed")
    run.skip("AWS Console/destroy", "Historical logs exist; no new paid lab authorized or run by this helper")
    run.skip("CI/Trivy/GHCR and cluster monitoring", "Requires actual pipeline/browser evidence; local checks do not substitute")
    run.save()
    print(f"\nEvidence saved: {run.output}\nReview README.md and every image before submission.")
    return 1 if any(item["status"] == "FAILED / BLOCKED" for item in run.records) else 0


if __name__ == "__main__":
    raise SystemExit(main())
