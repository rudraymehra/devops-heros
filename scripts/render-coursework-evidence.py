"""Render source-linked images of our actual records, never pretend screen captures.

Uses the existing offline macOS text renderer. Does not run Docker, AWS, or any
reference ZIP code. Rendered images are kept separate from native screenshots.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile
import textwrap
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("coursework", ROOT / "scripts/coursework-evidence.py")
coursework = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coursework)
NATIVE_NOTICE = "RENDERED EXECUTION LOG — NOT a native Terminal or AWS Console screenshot"

# Only actual recorded command blocks are selected. Limits avoid repeated JSON
# polling; the complete unchanged source is linked from every image's index.
HISTORY = {
    "09": [("submissions/09-kubernetes-fundamentals/OUTPUT.md", r"version --client|cluster-info|get nodes|get pods -n kube-system|get pod hello|logs hello", 6)],
    "10": [("submissions/10-kubernetes-core-objects/OUTPUT.md", r"objects.yaml|get pods,replicasets|delete pod|scale deployment|set image|rollout history|rollout undo|get pods,rs", 8),
           ("submissions/10-kubernetes-core-objects/STRATEGIES-SUCCESS.md", r"get endpointslices|get pods.*track|get pods.*version", 3)],
    "11": [("submissions/11-kubernetes-services/OUTPUT.md", r"get services|nslookup|patch service|apply -f.*services.yaml", 7)],
    "12": [("submissions/12-kubernetes-config-ingress/OUTPUT.md", r"get configmaps|describe secret|describe ingress|exec deployment/homework-backend.*urllib", 5)],
    "13": [("session21-python/evidence/eks-verification.md", r"rollout status deployment/taskboard-postgres|get pvc", 2),
           ("session21-python/evidence/scaling-and-probes.md", r"describe pod campusfix-probes", 1)],
    "14": [("submissions/14-troubleshooting/OUTPUT.md", r"get pods -o wide|logs fail-.*--tail=10", 7)],
    "15": [("submissions/15-helm/OUTPUT.md", r"^\$ helm .* (install|upgrade|history|rollback|uninstall) ", 7)],
    "18": [("submissions/18-terraform/OUTPUT.md", r"terraform (init|validate|plan|apply) ", 4),
           ("submissions/18-terraform/DESTROY-RETRY.md", r"terraform destroy ", 1)],
    "19": [("submissions/19-cloud/OUTPUT-SUCCESS.md", r"terraform (init|validate|plan|apply|destroy|state list)", 6)],
    "20": [("session21-python/evidence/eks-verification.md", r"get configmap taskboard-config| get application campusfix| get pods -n monitoring", 3)],
}


def numbered(lines, start=0, end=None):
    end = len(lines) if end is None else end
    indices = list(range(start, end))
    if len(indices) > 48:
        indices = indices[:18] + [None] + indices[-26:]
    return "\n".join(
        "[... source lines omitted for readability; see complete linked record ...]" if i is None
        else f"{i + 1:05d}  {lines[i].expandtabs(4)}" for i in indices
    )


def command_blocks(lines):
    starts = [i for i, line in enumerate(lines) if line.startswith("$ ")]
    return [(start, starts[n + 1] if n + 1 < len(starts) else len(lines)) for n, start in enumerate(starts)]


def render(renderer, directory, slug, title, source, body, evidence_type, note):
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    relative = source.relative_to(ROOT).as_posix()
    badge = NATIVE_NOTICE if evidence_type != "recorded-ci-metadata" else "RENDERED CI METADATA — NOT a native screenshot or command-output log"
    document = f"""{badge}

Rudray Mehra | 24 BCS 10425 | Batch B
{title}
Evidence type: {evidence_type}
{note}
Historical resource names and outcomes are not rewritten. This image does not prove a current live deployment.
Source: {relative}
Source SHA-256: {digest}
Image rendered: {datetime.now(timezone.utc).isoformat()}

{body}
"""
    wrapped = "\n".join("\n".join(textwrap.wrap(line, width=176, replace_whitespace=False,
                                                drop_whitespace=False)) for line in document.splitlines()) + "\n"
    text_path, image_path = directory / (slug + ".txt"), directory / (slug + ".png")
    text_path.write_text(wrapped)
    subprocess.run([str(renderer), str(text_path), str(image_path)], check=True)
    if not image_path.read_bytes().startswith(coursework.native.PNG_SIGNATURE):
        raise RuntimeError("Renderer did not create a PNG: " + str(image_path))
    return {"title": title, "image": image_path.name, "image_sha256": coursework.native.file_hash(image_path),
            "text": text_path.name, "source": relative, "source_sha256": digest,
            "kind": evidence_type, "native_screenshot": False}


def main():
    gallery = ["# Rendered coursework evidence — Rudray Mehra", "", "24 BCS 10425 · Batch B", "",
               "These are images of our own actual records, **not native Terminal screenshots**.",
               "Failures remain failures. Historical cloud records are dated 2026-10-13; the cloud lab was destroyed.",
               "CI metadata views show only a recorded workflow result, not missing per-command output.",
               "Ask the instructor before substituting these for a native screenshot requirement.", ""]
    count = 0
    with tempfile.TemporaryDirectory(prefix="rudray-evidence-render-") as build:
        renderer = Path(build) / "render-log-text"
        subprocess.run(["clang", str(ROOT / "session21-python/scripts/render-log-text.c"), "-o", str(renderer),
                        "-framework", "CoreFoundation", "-framework", "CoreGraphics",
                        "-framework", "CoreText", "-framework", "ImageIO"], check=True)
        for item in coursework.CATALOG:
            key = item["key"]
            parent = (ROOT / item["readme"]).parent / "screenshots"
            directory = parent / "rendered-log-views"
            directory.mkdir(parents=True, exist_ok=True)
            entries = []
            # Latest real local run. No synthetic output or reference README snippets.
            runs = sorted(parent.glob("rudray-*/manifest.json"))
            if runs:
                metadata = json.loads(runs[-1].read_text())
                for record in metadata["records"]:
                    if not record.get("log"):
                        continue
                    source = runs[-1].parent / record["log"]
                    if coursework.native.file_hash(source) != record["log_sha256"]:
                        raise RuntimeError("Source log changed: " + str(source))
                    entries.append(render(renderer, directory, "local-" + source.stem, record["title"], source,
                                          numbered(source.read_text().splitlines()), "local-recorded-command",
                                          "Actual recorded result: " + record["status"] + "; this is a log rendering, not a new execution."))
            for source_name, pattern, limit in HISTORY.get(key, []):
                source = ROOT / source_name
                lines = source.read_text().splitlines()
                selected = [(start, end) for start, end in command_blocks(lines) if re.search(pattern, lines[start])][:limit]
                if not selected:
                    raise RuntimeError(f"No actual command matched {key}: {source_name}: {pattern}")
                for start, end in selected:
                    slug = f"historical-{source.stem.lower()}-line-{start + 1}"
                    entries.append(render(renderer, directory, slug, f"Session {key} — recorded command excerpt", source,
                                          numbered(lines, start, end), "historical-command-excerpt",
                                          "Historical 2026-10-13 run; lab already destroyed. Line numbers identify the unchanged source excerpt."))
            if key in {"06", "07", "08", "16", "17"}:
                source = ROOT / "session21-python/evidence/published/ci-runs.json"
                field = "foundation" if key in {"06", "07", "08"} else "session" + key
                data = json.loads(source.read_text())[field]
                entries.append(render(renderer, directory, "recorded-ci-result", f"Session {key} — recorded CI result (metadata only)", source,
                                      json.dumps(data, indent=2), "recorded-ci-metadata",
                                      "Selected recorded JSON object: " + field + ". Not a fresh CI check, Docker build log, or Trivy report."))
            if key == "20":
                source = ROOT / "session21-python/evidence/observability/result.json"
                data = json.loads(source.read_text())
                selected = {"timestamp": data["timestamp"], "status": data["status"], "targets": [
                    {k: target.get(k) for k in ("labels", "health", "lastError", "scrapeUrl")} for target in data["targets"]]}
                entries.append(render(renderer, directory, "recorded-prometheus-targets", "Session 20 — recorded Prometheus target fields", source,
                                      json.dumps(selected, indent=2), "historical-monitoring-json",
                                      "Selected actual JSON fields, not a fabricated curl command or live Targets page."))
            (directory / "manifest.json").write_text(json.dumps(entries, indent=2) + "\n")
            lines = [f"# Session {key} — rendered recorded evidence", "", "Rudray Mehra · 24 BCS 10425 · Batch B", "",
                     "**Not native screenshots.** These PNGs render source-linked records. Historic resources are offline; failed attempts are not passes.",
                     "Current name in the heading identifies the submission. Old command/resource labels remain unchanged in excerpts.", ""]
            for entry in entries:
                lines += ["## " + entry["title"], "", "Type: `" + entry["kind"] + "`.",
                          f"[Original source]({coursework.link_from(directory, entry['source'])}) · [Rendered text]({entry['text']})", "",
                          f"![Rendered recorded evidence, not a native screenshot]({entry['image']})", ""]
            (directory / "README.md").write_text("\n".join(lines))
            gallery.append(f"- [Session {key}: {len(entries)} rendered images]({coursework.link_from(ROOT / 'evidence/coursework', str((directory / 'README.md').relative_to(ROOT)))})")
            count += len(entries)
            print(f"Session {key}: {len(entries)} labelled record images", flush=True)
    gallery += ["", f"Total: **{count} rendered images**. Native capture counts remain separate.", ""]
    (ROOT / "evidence/coursework/RENDERED-LOG-GALLERY.md").write_text("\n".join(gallery))
    coursework.audit()
    print(f"Created {count} PNG images from actual records. Native screenshots created: 0.")


if __name__ == "__main__":
    main()
