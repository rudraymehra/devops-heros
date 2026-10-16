"""Non-executing Python/shell syntax checks across the coursework source folders."""
import ast
import importlib.util
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("coursework", root / "scripts/coursework-evidence.py")
coursework = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coursework)
roots = sorted({name for item in coursework.CATALOG for name in item["roots"]})
listed = subprocess.run(["rg", "--files", *roots, "-g", "*.py", "-g", "*.sh"],
                        cwd=root, capture_output=True, text=True, check=True)
failed = []
checked = sorted(set(listed.stdout.splitlines()))
print("Rudray Mehra | 24 BCS 10425 | Batch B")
print("Static syntax only — not runtime, deployment, vulnerability or screenshot proof.")
for name in checked:
    path = root / name
    try:
        if path.suffix == ".py":
            ast.parse(path.read_text(), filename=name)
        else:
            result = subprocess.run(["bash", "-n", str(path)], capture_output=True, text=True)
            if result.returncode:
                raise ValueError(result.stderr.strip())
        print("SYNTAX OK:", name)
    except (SyntaxError, ValueError) as error:
        failed.append(name)
        print("SYNTAX FAILED:", name, str(error))
print(f"Checked {len(checked)} source files; syntax failures: {len(failed)}")
raise SystemExit(bool(failed))
