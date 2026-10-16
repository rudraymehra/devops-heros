"""Save an actual command and its output as Markdown evidence."""
import argparse
import re
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("output", type=Path)
parser.add_argument("--cwd", default=".")
parser.add_argument("command", nargs=argparse.REMAINDER)
args = parser.parse_args()
command = args.command[1:] if args.command[:1] == ["--"] else args.command
if not command:
    parser.error("a command after -- is required")
result = subprocess.run(command, cwd=args.cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
redacted = re.sub(r"\b\d{12}\b", "[AWS_ACCOUNT_ID]", result.stdout)
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(
    "# Command evidence\n\nStudent: Rudray Mehra · 24 BCS 10425 · Batch B\n\n"
    + "Captured: " + datetime.now(timezone.utc).isoformat() + "\n\n"
    + "Working directory: " + args.cwd + "\n\n"
    + "```text\n$ " + shlex.join(command) + "\n" + redacted + "\n```\n\n"
    + "Exit code: " + str(result.returncode) + "\n"
)
print(str(args.output) + ": exit " + str(result.returncode))
raise SystemExit(result.returncode)
