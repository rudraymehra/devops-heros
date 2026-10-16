"""Audit Sessions 1–20 against a reference ZIP and capture only actual commands.

The ZIP is read as data; none of its code or screenshots is imported or executed.
Native captures use the existing macOS window selector and require --screenshots.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("native_capture", ROOT / "session21-python/scripts/capture-native-evidence.py")
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
PYTHON = str(ROOT / "session21-python/backend/.venv/bin/python")
FOUNDATION = "https://github.com/rudraymehra/devops-heros/actions/runs/38372002674"
CAPSTONE = "session21-python/evidence/"


def entry(key, reference, readme, roots, required, historical, pending):
    return dict(key=key, reference=reference, readme=readme, roots=roots,
                required=required, historical=historical, pending=pending)


CATALOG = [
    entry("01-02", "session-01-02-linux", "session2-linux/README.md", ["session2-linux"],
          ["session2-linux/session2.md", "session2-linux/Linux Networking Cheat Sheet.pdf"], [FOUNDATION],
          "Linux useradd/adduser and journalctl need a real Linux/systemd environment. macOS link tests are labelled macOS, not Linux VM results."),
    entry("03", "session-03-shell-scripting", "session3-shell-scripting/README.md", ["session3-shell-scripting"],
          ["session3-shell-scripting/system-info.sh"], [FOUNDATION],
          "Capture the actual system-info script and process/report files. Process arguments are omitted to avoid exposing credentials."),
    entry("04", "session-04-networking", "session4-networking/README.md", ["session4-networking"],
          ["session4-networking/collect-network-info.sh"], [FOUNDATION],
          "Capture routes, sockets, DNS, ping and HTTP on the actual host. Record network restrictions as failures, not successful connectivity."),
    entry("05", "session-05-git-github", "session5-git-github/README.md", ["session5-git-github"],
          ["session5-git-github/run-cherry-pick-lab.sh"], [FOUNDATION],
          "Capture real commit -a status and cherry-pick graph in the disposable lab, not the dirty coursework repository."),
    entry("06", "session-06-docker-fundamentals", "session6-7-docker/README.md", ["session6-7-docker"],
          [f"session6-7-docker/{name}/Dockerfile" for name in ["nodejs-app", "python-app", "java-app", "Apache-app", "React-app", "nginx-app"]],
          [FOUNDATION], "Docker must be running. Capture six real image builds, HTTP responses, container state and corresponding browser pages."),
    entry("07", "session-07-docker-images", "session6-7-docker/multi-stage-dockerfile/README.md", ["session6-7-docker/multi-stage-dockerfile"],
          ["session6-7-docker/multi-stage-dockerfile/Dockerfile"], [FOUNDATION],
          "Capture the actual multi-stage image build, image metadata, running application and browser. App-type discussion is documentation, not runtime proof."),
    entry("08", "session-08-docker-networking", "session8-docker-networking-volume/README.md", ["session8-docker-networking-volume"],
          ["session8-docker-networking-volume/demo/docker-compose.yml", "session8-docker-networking-volume/bind-mount/docker-compose.yml", "session8-docker-networking-volume/host-network/docker-compose.yml"],
          [FOUNDATION], "Capture Compose networks/connectivity. Bind-mount edit/reload and host-network behaviour need their own live run; Docker Desktop host networking may need explicit support."),
    entry("09", "session-09-kubernetes-fundamentals", "submissions/09-kubernetes-fundamentals/README.md", ["submissions/09-kubernetes-fundamentals"],
          ["submissions/09-kubernetes-fundamentals/pod.yaml", "submissions/09-kubernetes-fundamentals/namespace.yaml"],
          ["submissions/09-kubernetes-fundamentals/OUTPUT.md"], "Capture actual cluster-info, nodes and Pods. Architecture explanations are not screenshots of a live cluster."),
    entry("10", "session-10-k8s-pods-replicasets-deployments", "submissions/10-kubernetes-core-objects/README.md", ["submissions/10-kubernetes-core-objects", "session10-k8s-core-objects"],
          ["submissions/10-kubernetes-core-objects/objects.yaml"], ["submissions/10-kubernetes-core-objects/OUTPUT.md", "submissions/10-kubernetes-core-objects/STRATEGIES-SUCCESS.md"],
          "Native lifecycle/rolling/blue-green/canary/Recreate sequence captures still need a live run. A current get snapshot alone does not prove those transitions."),
    entry("11", "session-11-k8s-networking-services", "submissions/11-kubernetes-services/README.md", ["submissions/11-kubernetes-services", "session-11-kubernetes-services"],
          ["submissions/11-kubernetes-services/services.yaml"], ["submissions/11-kubernetes-services/OUTPUT.md"],
          "Capture five Service types, DNS/HTTP and endpoint checks; an external LoadBalancer address needs a real controller/tunnel, not an invented IP."),
    entry("12", "session-12-k8s-ingress-configmaps-secrets", "submissions/12-kubernetes-config-ingress/README.md", ["submissions/12-kubernetes-config-ingress", "session-12-ingress-configmaps-secrets"],
          ["submissions/12-kubernetes-config-ingress/" + name for name in ["app.yaml", "configmap.yaml", "secret.yaml", "ingress.yaml"]],
          ["submissions/12-kubernetes-config-ingress/OUTPUT.md"], "Capture ConfigMap/Secret metadata and actual ingress requests, plus the failure/recovery exercises. Never screenshot decoded real Secret values."),
    entry("13", "session-13-k8s-storage-hpa-probes", "submissions/13-storage-hpa-probes/README.md", ["session-13-storage-hpa-probes", "submissions/13-storage-hpa-probes"],
          ["session-13-storage-hpa-probes/SUBMISSION.md"], [CAPSTONE + "eks-verification.md", CAPSTONE + "scaling-and-probes.md"],
          "Capture real PVC persistence, HPA scale up/down and probe recovery. The older EKS results use integrated CampusFix and retain their original timestamps."),
    entry("14", "session-14-k8s-troubleshooting", "submissions/14-troubleshooting/README.md", ["session-14-kubernetes-troubleshooting", "submissions/14-troubleshooting"],
          ["session-14-kubernetes-troubleshooting/scenarios/triage_all.sh"], ["submissions/14-troubleshooting/OUTPUT.md"],
          "Five scenarios were recorded previously; the ZIP also names service, pod-network and ContainerCreating cases. Those additional live demonstrations are not certified by the five-scenario log."),
    entry("15", "session-15-helm", "submissions/15-helm/README.md", ["session-15-helm", "submissions/15-helm"],
          ["session-15-helm/mini-project/notes-chart/Chart.yaml"], ["submissions/15-helm/OUTPUT.md"],
          "Lint/template can run offline. Install, upgrade, history, rollback and uninstall screenshots require their actual lifecycle, not lint output."),
    entry("16", "session-16-cicd-github-actions", "submissions/16-cicd/README.md", ["session-16-github-actions", "submissions/16-cicd"],
          [".github/workflows/session16-ci.yml", "session-16-github-actions/session-16-github-actions/10-final-cicd-pipeline/tests/test_calculator.py"],
          ["https://github.com/rudraymehra/devops-heros/actions/runs/38341620592", CAPSTONE + "published/session16-ci.png"],
          "Capture current tests/build and the actual GitHub Actions run. Local act simulation is not a substitute for a published workflow."),
    entry("17", "session-17-cicd-devsecops", "submissions/17-devsecops/README.md", ["session-17-devsecops", "submissions/17-devsecops"],
          [".github/workflows/session17-devsecops.yml", "session-17-devsecops/demo/tests/test_app.py"],
          ["https://github.com/rudraymehra/devops-heros/actions/runs/38342666869", CAPSTONE + "published/session17-ci.png"],
          "Capture real unit/SAST/SCA/secret/image scan and deployment results. Before/after findings must come from real revisions; never invent a vulnerable scan."),
    entry("18", "session-18-terraform-iac", "submissions/18-terraform/README.md", ["session18-terraform-iac", "submissions/18-terraform"],
          ["session18-terraform-iac/terraform-s3-demo/main.tf"], ["submissions/18-terraform/OUTPUT.md", "submissions/18-terraform/DESTROY-RETRY.md"],
          "Original S3 apply/destroy logs exist, but native images were not captured. Validation now is not proof of that earlier apply/destroy. No paid lab is recreated automatically."),
    entry("19", "session-19-cloud-terraform", "submissions/19-cloud/README.md", ["session19-cloud-terraform", "submissions/19-cloud"],
          ["session19-cloud-terraform/08-mini-project/main.tf"], ["submissions/19-cloud/OUTPUT-SUCCESS.md"],
          "Original 11-resource apply/HTTP/destroy logs exist. New live AWS screenshots require a newly approved paid lab. The architecture image in the ZIP is not terminal evidence."),
    entry("20", "session-20-monitoring-observability-gitops", "submissions/20-monitoring-gitops/README.md", ["session20-monitoring-observability-gitops", "submissions/20-monitoring-gitops"],
          ["session20-monitoring-observability-gitops/03-prometheus/prometheus.yml", "session21-python/gitops/application.yaml"],
          [CAPSTONE + "observability/prometheus-targets.png", CAPSTONE + "observability/grafana-dashboard.png", CAPSTONE + "observability/argocd-synced.png", CAPSTONE + "eks-verification.md"],
          "Targets/dashboard/self-healing have historical evidence. New alert firing/recovery, cAdvisor and live cluster captures are not proven by those images; the cloud cluster is offline."),
]


def link_from(directory, target):
    if target.startswith("https://"):
        return target
    return os.path.relpath(ROOT / target, directory).replace(os.sep, "/").replace(" ", "%20")


def manifest_for_zip(path):
    """No extraction: only list each reference image and hash the archive."""
    with zipfile.ZipFile(path) as archive:
        images = [name for name in archive.namelist() if Path(name).suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
        groups = {item["key"]: [name for name in images if f"/{item['reference']}/" in name] for item in CATALOG}
    with path.open("rb") as stream:
        checksum = hashlib.file_digest(stream, "sha256").hexdigest()
    return {"archive": path.name, "sha256": checksum,
            "groups": groups, "note": "Reference filenames only; no reference image copied or claimed as our execution."}


def valid_native_file(directory, shot):
    if not shot or shot.get("file") != Path(shot.get("file", "")).name:
        return False
    path = directory / shot["file"]
    return (path.is_file() and path.read_bytes().startswith(native.PNG_SIGNATURE)
            and native.file_hash(path) == shot.get("sha256"))


def screenshot_review(directory, shot, reviews):
    """Bind visual decisions to exact bytes; rejection survives publication exclusion."""
    if not shot:
        return "not-captured", "No native image captured."
    filename = shot.get("file", "")
    if not filename or filename != Path(filename).name:
        return "invalid", "Invalid screenshot filename."
    key = (directory / filename).relative_to(ROOT).as_posix()
    review = reviews.get(key, {})
    if review.get("sha256") == shot.get("sha256") and review.get("decision") == "rejected":
        return "rejected", review["note"]
    if not valid_native_file(directory, shot):
        return "invalid", "Declared image missing or checksum differs."
    if review.get("sha256") == shot.get("sha256") and review.get("decision") == "accepted":
        return "accepted", review["note"]
    return "pending", "Visual review required; not counted as accepted evidence."


def reviewed_run_index(directory, run, reviews):
    """Regenerate navigation only; never modify raw logs, PNGs or capture manifests."""
    lines = ["# Fresh command evidence — reviewed index", "", native.IDENTITY, "",
             "Raw logs and capture manifests are unchanged. Visual decisions are hash-bound in",
             "[the review record](" + link_from(directory, "evidence/coursework/native-review.json") + ").",
             "Rejected images remain local and are excluded from publication. A pass is only for the named command.", ""]
    for record in run["records"]:
        lines += ["## " + record["title"], "", "Execution: " + record["status"] + ".", ""]
        if record.get("log"):
            lines += [f"[Original command output]({record['log']})", ""]
        shot = record.get("screenshot")
        decision, note = screenshot_review(directory, shot, reviews)
        lines += ["Native capture: **" + decision + "**. " + note, ""]
        if decision == "accepted":
            lines += [f"![Reviewed native window capture]({shot['file']})", ""]
    return "\n".join(lines)


def audit(zip_path=None):
    folder = ROOT / "evidence/coursework"
    folder.mkdir(parents=True, exist_ok=True)
    manifest_path = folder / "reference-manifest.json"
    if zip_path:
        manifest_path.write_text(json.dumps(manifest_for_zip(zip_path), indent=2) + "\n")
    reference = json.loads(manifest_path.read_text())
    review_path = folder / "native-review.json"
    reviews = json.loads(review_path.read_text())["images"] if review_path.exists() else {}
    rows = []
    results = []
    for item in CATALOG:
        directory = (ROOT / item["readme"]).parent / "screenshots"
        directory.mkdir(parents=True, exist_ok=True)
        missing = [name for name in [item["readme"], *item["required"]] if not (ROOT / name).is_file()]
        images = reference["groups"][item["key"]]
        records = []
        for path in sorted(directory.glob("rudray-*/manifest.json")):
            records.append((path, json.loads(path.read_text())))
        decisions = [screenshot_review(path.parent, r.get("screenshot"), reviews)[0]
                     for path, run in records for r in run["records"]]
        accepted, pending, rejected = (decisions.count(kind) for kind in ("accepted", "pending", "rejected"))
        row = {"session": item["key"], "required_files_missing": missing,
               "reference_images": len(images), "native_files_accepted": accepted,
               "native_files_pending_review": pending, "native_files_rejected": rejected,
               "runs": [str(path.parent.relative_to(ROOT)) for path, _ in records], "pending": item["pending"]}
        results.append(row)
        lines = [f"# Session {item['key']} — evidence and screenshots", "", native.IDENTITY, "",
                 "Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.",
                 "No reference screenshot has been relabelled. A command log is not a native screenshot.", "",
                 f"Required entry point/core-file checks: {'MISSING: ' + ', '.join(missing) if missing else 'all listed files present (not a runtime pass)' }.",
                 f"Reference images: {len(images)}. Native captures: {accepted} accepted; {pending} awaiting review; {rejected} rejected.", "",
                 "## Fresh execution records", ""]
        if not records:
            lines.append("No fresh run recorded here yet. Native terminal captures remain pending.")
        for path, run in records:
            relative = path.parent.relative_to(directory).as_posix()
            if any((path.parent / r.get("screenshot", {}).get("file", "")).relative_to(ROOT).as_posix() in reviews
                   for r in run["records"] if r.get("screenshot")):
                (path.parent / "README.md").write_text(reviewed_run_index(path.parent, run, reviews))
            lines += [f"### [{path.parent.name}]({relative}/README.md)", ""]
            for record in run["records"]:
                if record.get("log"):
                    lines.append(f"- [{record['title']}]({relative}/{record['log']}): {record['status']}.")
                shot = record.get("screenshot")
                decision, note = screenshot_review(path.parent, shot, reviews)
                if decision == "accepted":
                    lines += ["", "Reviewed native capture: " + note, "",
                              f"![Reviewed native window capture]({relative}/{shot['file']})", ""]
                elif shot:
                    lines.append("- Native capture " + decision.upper() + ": " + note)
                elif not record.get("log"):
                    lines.append(f"- {record['title']}: {record['status']}.")
            lines += [""]
        rendered = directory / "rendered-log-views/README.md"
        if rendered.exists():
            lines += ["", "## Rendered record images (not native screenshots)", "",
                      "[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).",
                      "These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.", ""]
        lines += ["", "## Existing historical evidence", ""]
        for target in item["historical"]:
            lines.append(f"- [{Path(target).name if not target.startswith('https:') else 'Earlier GitHub Actions run'}]({link_from(directory, target)})")
        lines += ["", "Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.",
                  "", "## Still needs genuine capture", "", item["pending"], "",
                  "Use the [coursework capture guide](" + link_from(directory, "COURSEWORK-EVIDENCE.md") + "). The helper displays Rudray Mehra around freshly executed commands.",
                  "", "## Reference image inventory (not copied)", ""]
        lines += ["- `" + name.split("/" + item["reference"] + "/", 1)[1] + "`" for name in images]
        lines += ["", "## Checked source files", ""]
        lines += [f"- [{Path(name).name}]({link_from(directory, name)})" for name in item["required"]]
        (directory / "README.md").write_text("\n".join(lines) + "\n")
        url = link_from(folder, str((directory / "README.md").relative_to(ROOT)))
        rows.append(f"| {item['key']} | {len(images)} | {'Missing files' if missing else 'Present'} | {accepted} | {pending} | {rejected} | [Evidence]({url}) |")
    report = ["# Sessions 1–20 — screenshot audit", "", native.IDENTITY, "",
              f"Compared all **{sum(len(v) for v in reference['groups'].values())} reference images** in the supplied ZIP against all 19 homework entry points (Sessions 1 and 2 share one).",
              "Core-file presence is not execution success. Accepted counts mean visual review of those images only, not full session completion.",
              "Rejected wrong-window images are kept locally but excluded from publication. Renderings are counted separately.",
              "", "| Session | ZIP images | Core files | Native accepted | To review | Rejected | Details |", "|---|---:|---|---:|---:|---:|---|"] + rows
    report += ["", "See [capture instructions](../../COURSEWORK-EVIDENCE.md). Each session page lists every reference image, actual local results, historical evidence and remaining gaps.",
               "", "Archive SHA-256: `" + reference["sha256"] + "`.", ""]
    if (folder / "RENDERED-LOG-GALLERY.md").exists():
        report += ["[Generated record-image gallery](RENDERED-LOG-GALLERY.md) — labelled renderings, not native screenshots.", ""]
    (folder / "README.md").write_text("\n".join(report))
    (folder / "audit.json").write_text(json.dumps(results, indent=2) + "\n")
    print(f"Audited {len(results)} homework groups; {sum(len(v) for v in reference['groups'].values())} reference images; no screenshots fabricated.")
    return results


def basics(topic):
    """Small actual host exercises; no administrator or private process arguments."""
    print(native.IDENTITY, flush=True)
    if topic == "links":
        with tempfile.TemporaryDirectory(prefix="rudray-link-lab-") as scratch:
            directory = Path(scratch)
            original, hard, soft = [directory / name for name in ("original.txt", "hard.txt", "soft.txt")]
            original.write_text("Rudray Mehra: link demonstration\n")
            os.link(original, hard)
            soft.symlink_to(original.name)
            subprocess.run(["ls", "-li", str(directory)], check=True)
            assert original.stat().st_ino == hard.stat().st_ino
            original.unlink()  # Only the file this exercise just created.
            assert hard.read_text() and not soft.exists() and soft.is_symlink()
            print("PASS: hard link shares the inode and survives unlink; symlink becomes dangling.")
            print("Actual host: " + sys.platform + "; this is not evidence of a Linux VM or journalctl.")
    elif topic == "system-info":
        with tempfile.TemporaryDirectory(prefix="rudray-system-info-") as scratch:
            result = subprocess.run(["bash", str(ROOT / "session3-shell-scripting/system-info.sh")],
                                    cwd=scratch, input="Rudray Mehra\n24 BCS 10425\n", text=True)
            if result.returncode:
                return result.returncode
            report = Path(scratch) / "system-info-output/report.txt"
            processes = Path(scratch) / "system-info-output/processes.txt"
            assert "Rudray Mehra" in report.read_text() and processes.stat().st_size > 0
            print("PASS: both real output files created; process arguments were excluded. Temporary test files removed after verification.")
    return 0


def run_sessions(args):
    if args.screenshots and (sys.platform != "darwin" or not sys.stdin.isatty()):
        raise SystemExit("Native screenshots require an interactive macOS Terminal.")
    selected = args.sessions.split(",") if args.sessions != "all" else [item["key"] for item in CATALOG]
    unknown = set(selected) - {item["key"] for item in CATALOG}
    if unknown:
        raise SystemExit("Unknown sessions: " + ", ".join(sorted(unknown)))
    stamp = datetime.now().strftime("rudray-%Y%m%d-%H%M%S-%f")
    docker = native.executable("docker", "/Applications/Docker.app/Contents/Resources/bin/docker")
    engine = None
    total_failed = 0
    for item in CATALOG:
        key = item["key"]
        if key not in selected:
            continue
        run = native.EvidenceRun((ROOT / item["readme"]).parent / "screenshots" / stamp, args.screenshots)
        def check(slug, title, command, cwd=ROOT, timeout=120):
            return run.check(slug, "Session " + key + " — " + title, command, cwd, timeout)
        if key == "01-02":
            check("01-links", "real hard/symbolic links on this host", [sys.executable, __file__, "basics", "links"])
            check("02-host", "actual OS/kernel", ["uname", "-a"])
            check("03-disk", "actual disk usage", ["df", "-h", str(ROOT)])
            run.skip("Linux user management and journalctl", "Requires Linux/systemd; no host users created")
        elif key == "03":
            check("01-syntax", "shell script syntax", ["bash", "-n", "session3-shell-scripting/system-info.sh"])
            check("02-system-info", "actual script with identity input", [sys.executable, __file__, "basics", "system-info"])
        elif key == "04":
            commands = [("01-route", ["/sbin/route", "-n", "get", "default"]), ("02-sockets", ["netstat", "-an", "-p", "tcp"])] if sys.platform == "darwin" else [("01-route", ["ip", "route"]), ("02-sockets", ["ss", "-tuln"])]
            commands += [("03-dns", ["dig", "+time=3", "+tries=1", "example.com"]),
                         ("04-ping", ["ping", "-c", "2", "1.1.1.1"]),
                         ("05-http", ["curl", "--head", "--fail", "--max-time", "10", "https://example.com"])]
            for slug, command in commands:
                check(slug, "actual " + slug, command, timeout=15)
        elif key == "05":
            check("01-commit-and-cherry-pick", "actual isolated Git lab", ["bash", "session5-git-github/run-cherry-pick-lab.sh"])
        elif key in {"06", "07", "08"}:
            if not args.docker_labs:
                run.skip("Docker live labs", "Add --docker-labs; never inferred from file presence")
            elif shutil.disk_usage(ROOT).free < 8 * 1024 ** 3:
                run.skip("Docker live labs", "Less than 8 GiB free; make room before building images. No data deleted automatically")
            else:
                if engine is None:
                    engine = check("00-engine", "Docker client/server", [docker, "version"], timeout=20)
                if not engine:
                    run.skip("Docker live labs", "Docker socket unavailable; open Docker Desktop and retry")
                elif key in {"06", "07"}:
                    apps = [("nodejs-app", 3000), ("python-app", 8000), ("java-app", 8080), ("Apache-app", 80), ("React-app", 80), ("nginx-app", 80)] if key == "06" else [("multi-stage-dockerfile", 8080)]
                    for index, (app, port) in enumerate(apps):
                        name = f"rudray-hw-{key}-{os.getpid()}-{index}"
                        image = f"rudray-homework-{app.lower()}:local"
                        if not check(app + "-build", "build " + app, [docker, "build", "-t", image, "session6-7-docker/" + app], timeout=900):
                            continue
                        started = check(app + "-run", "start " + app, [docker, "run", "-d", "--name", name, "--label", "devops.evidence=rudray", "-p", f"127.0.0.1::{port}", image], timeout=60)
                        if not started:
                            continue
                        try:
                            code, output = native.execute([docker, "port", name, f"{port}/tcp"], ROOT, 20)
                            address = output.strip()
                            if code or not re.fullmatch(r"127\.0\.0\.1:\d+", address):
                                run.skip(app + " HTTP", "Could not resolve its loopback port")
                                continue
                            url = "http://" + address
                            check(app + "-http", "actual HTTP response", ["curl", "--fail", "--retry", "8", "--retry-all-errors", "--retry-delay", "2", "--max-time", "10", url], timeout=120)
                            check(app + "-status", "actual container/image", [docker, "ps", "--filter", "name=" + name], timeout=20)
                            if args.screenshots:
                                subprocess.run(["open", url], check=False)
                                shot = native.capture_window(run.output / (app + "-browser.png"), "Actual " + app + " browser")
                                run.records.append({"title": app + " browser", "status": "VISUAL REVIEW REQUIRED", "screenshot": shot})
                                run.save()
                        finally:
                            # Target only the uniquely named container created above, never other projects/volumes.
                            check(app + "-stop", "stop this temporary container only", [docker, "stop", "--time", "5", name], timeout=20)
                            check(app + "-remove", "remove this disposable container (no volumes)", [docker, "rm", name], timeout=20)
                else:
                    compose = [docker, "compose", "-p", "rudray-hw08", "-f", "session8-docker-networking-volume/demo/docker-compose.yml"]
                    check("01-compose", "three-network stack startup", compose + ["up", "--build", "-d", "--wait", "--wait-timeout", "180"], timeout=900)
                    check("02-status", "actual Compose services", compose + ["ps", "--all"], timeout=30)
                    check("03-networks", "actual network topology", [docker, "network", "inspect", "rudray-hw08_frontend_net", "rudray-hw08_backend_net", "rudray-hw08_database_net"], timeout=30)
                    check("04-connectivity", "backend reaches database", compose + ["exec", "-T", "backend", "python", "-c", "import socket; s=socket.create_connection(('database',3306),10); print('Database reachable'); s.close()"], timeout=30)
                    check("05-stop", "stop lab and preserve database volume", compose + ["down"], timeout=90)
                    run.skip("Host network and bind edit/reload", "Not performed by this mode; original CI evidence remains separate")
        elif key == "15":
            chart = "session-15-helm/mini-project/notes-chart"
            check("01-helm-lint", "real chart lint (not install)", [native.executable("helm"), "lint", chart])
            check("02-helm-template", "actual template rendering (not install)", [native.executable("helm"), "template", "rudray-notes", chart])
        elif key in {"16", "17"}:
            project = ROOT / ("session-16-github-actions/session-16-github-actions/10-final-cicd-pipeline" if key == "16" else "session-17-devsecops/demo")
            python = args.python17 if key == "17" and args.python17 else PYTHON
            check("01-pytest", "actual project tests", [python, "-m", "pytest", "-v"], project)
            if key == "17":
                check("02-bandit", "actual source scan", [python, "-m", "bandit", "-r", "app"], project)
            if args.ci_logs:
                workflow = "session16-ci.yml" if key == "16" else "session17-devsecops.yml"
                check("03-ci-status", "actual GitHub run listing", ["gh", "run", "list", "--repo", "rudraymehra/devops-heros", "--workflow", workflow, "--limit", "5"], timeout=30)
            run.skip("CI/image/security/deployment screenshots", "Use actual jobs for the submitted SHA; local test success alone is not CI success")
        elif key in {"18", "19"}:
            project = ROOT / ("session18-terraform-iac/terraform-s3-demo" if key == "18" else "session19-cloud-terraform/08-mini-project")
            terraform = args.terraform or shutil.which("terraform")
            if terraform:
                check("01-format", "Terraform format check", [terraform, "fmt", "-check"], project)
                check("02-validate", "actual Terraform validate (not apply)", [terraform, "validate", "-no-color"], project, timeout=60)
            else:
                run.skip("Terraform validation", "Supply --terraform /path/to/terraform")
            run.skip("AWS plan/apply/output/destroy screenshots", "Old lab destroyed; no cloud apply/destroy performed")
        if key in {"09", "10", "11", "12", "13", "14", "15", "20"}:
            if args.kube_context:
                namespace = {"13": "taskboard", "14": "campusfix-troubleshooting", "15": "campusfix-helm", "20": "monitoring"}.get(key, "rudray-devops-hw")
                base = ["kubectl", "--context", args.kube_context, "--request-timeout=15s"]
                if key == "09":
                    check("03-cluster", "actual cluster info", base + ["cluster-info"], timeout=30)
                    check("04-nodes", "actual nodes", base + ["get", "nodes", "-o", "wide"], timeout=30)
                resource = {"10": "pods,rs,deployments", "11": "services,endpointslices", "12": "configmaps,secrets,ingress", "13": "pods,pvc,hpa", "14": "pods,events", "20": "pods,services"}.get(key, "pods")
                check("05-kubernetes-state", "actual state; inspect contents, not just exit code", base + ["-n", namespace, "get", resource], timeout=30)
                if key == "15":
                    check("06-helm-list", "actual releases", ["helm", "list", "--kube-context", args.kube_context, "-n", namespace], timeout=30)
                if key == "20":
                    check("06-argocd", "actual GitOps sync state", base + ["-n", "argocd", "get", "applications"], timeout=30)
                run.skip("Lifecycle/failure/scale transitions", "Read-only snapshots do not demonstrate the earlier event sequence; see session gap list")
            else:
                run.skip("Live Kubernetes/Helm/monitoring capture", "No explicit --kube-context provided; historical EKS lab was destroyed")
        run.skip("Reference-specific pending items", item["pending"])
        run.save()
        total_failed += sum(r["status"] == "FAILED / BLOCKED" for r in run.records)
    audit()
    print("Capture run finished. Failures:", total_failed, "Review each session/screenshots/README.md; NOT RUN is not completion.")
    return 1 if total_failed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    audit_parser = sub.add_parser("audit")
    audit_parser.add_argument("--zip", type=Path)
    local = sub.add_parser("basics")
    local.add_argument("topic", choices=["links", "system-info"])
    run = sub.add_parser("run")
    run.add_argument("--sessions", default="all", help="all or comma-separated keys, e.g. 01-02,03,05,15,16")
    run.add_argument("--screenshots", action="store_true")
    run.add_argument("--docker-labs", action="store_true", help="Build/start scoped local labs; stop own containers, preserve DB volumes")
    run.add_argument("--kube-context", help="Read-only state checks against an explicitly selected cluster; no cluster creation")
    run.add_argument("--terraform")
    run.add_argument("--python17", help="Interpreter with Session 17 Flask/pytest/Bandit dependencies")
    run.add_argument("--ci-logs", action="store_true", help="Read actual GitHub run listings using existing gh login")
    args = parser.parse_args()
    if args.mode == "audit":
        audit(args.zip)
        return 0
    if args.mode == "basics":
        return basics(args.topic)
    return run_sessions(args)


if __name__ == "__main__":
    raise SystemExit(main())
