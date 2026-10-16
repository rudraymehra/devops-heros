"""Render traceable excerpts of this repository's actual logs, never fake terminals.

Requires macOS Command Line Tools. Source logs are read-only. Every image identifies
its source, source checksum, capture date and whether the evidence is historical.
"""
import hashlib
import json
import subprocess
import tempfile
import textwrap
from datetime import datetime, timezone
from pathlib import Path

project = Path(__file__).resolve().parents[1]
evidence = project / "evidence"
output = evidence / "recorded-log-views"
output.mkdir(parents=True, exist_ok=True)


def excerpt(filename, sections):
    path = evidence / filename
    lines = path.read_text().splitlines()
    result = []
    for start, end in sections:
        start = max(0, len(lines) + start) if start < 0 else start
        end = len(lines) if end is None else end
        if result:
            result.append("[... intervening source lines omitted; see linked full log ...]")
        result.extend(f"{i + 1:04d}  {lines[i]}" for i in range(start, min(end, len(lines))))
    return path, "\n".join(result)


cards = [
    ("terraform-plan", "Terraform plan — recorded result", *excerpt("aws-plan.md", [(0, 17), (-40, None)])),
    ("terraform-destroy", "Terraform destroy — recorded result", *excerpt("aws-destroy.md", [(0, 10), (-38, None)])),
    ("eks-pods-services", "EKS Pods, Services and storage — recorded result", *excerpt("eks-verification.md", [(0, 37)])),
    ("eks-helm-deployment", "EKS Helm installation — recorded result", *excerpt("eks-helm-deploy.md", [(0, None)])),
]
metrics_path = evidence / "observability/result.json"
metrics = json.loads(metrics_path.read_text())
targets = {
    "timestamp": metrics["timestamp"],
    "status": metrics["status"],
    "targets": [
        {key: target.get(key) for key in ("labels", "health", "lastError", "scrapeUrl")}
        for target in metrics["targets"]
    ],
}
cards.append(("prometheus-target-results", "Prometheus targets — selected recorded JSON fields", metrics_path,
              json.dumps(targets, indent=2)))
fresh_tests = evidence / "pytest-2026-10-16.md"
if fresh_tests.exists():
    cards.append(("pytest-2026-10-16", "Local pytest — captured execution log", *excerpt(fresh_tests.name, [(0, None)])))

created = datetime.now(timezone.utc).isoformat()
manifest = []
with tempfile.TemporaryDirectory(prefix="campusfix-log-render-") as build_dir:
    renderer = Path(build_dir) / "render-log-text"
    subprocess.run(["clang", str(project / "scripts/render-log-text.c"), "-o", str(renderer),
                    "-framework", "CoreFoundation", "-framework", "CoreGraphics",
                    "-framework", "CoreText", "-framework", "ImageIO"], check=True)
    for slug, title, source, body in cards:
        source_name = source.relative_to(project).as_posix()
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        document = f"""RECORDED LOG VIEW — not a native terminal or AWS Console screenshot

{title}
Submission: Rudray Mehra · 24 BCS 10425 · Batch B
Original execution dates, historical labels and resource names are unchanged.
Historical cloud evidence does not imply a currently running deployment.
Source: {source_name}
SHA-256: {digest}
Rendered: {created}

{body}"""
        wrapped = "\n".join("\n".join(textwrap.wrap(line, width=176, replace_whitespace=False,
                                                    drop_whitespace=False)) for line in document.splitlines())
        text_file = output / (slug + ".txt")
        text_file.write_text(wrapped + "\n")
        subprocess.run([str(renderer), str(text_file), str(output / (slug + ".png"))], check=True)
        manifest.append({"image": slug + ".png", "source": source_name, "source_sha256": digest,
                         "rendered_at": created, "kind": "recorded-log-view", "title": title})
(output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"Rendered {len(manifest)} explicitly labelled evidence views to {output}")
