#!/usr/bin/env python3
"""Ask real Claude (one reply, no tools) each scenario with ONE plugin loaded, and check the reply against simple patterns.

    python3 tests/run_scenarios.py [plugin ...] [--model sonnet] [--show]

Needs the `claude` CLI signed in. Each scenario is one Claude call. Patterns are a smoke test, not a full judge:
read the replies too (--show)."""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NO_TOOLS = "Bash,PowerShell,Edit,Write,Read,Grep,Glob,Agent,WebSearch,WebFetch,NotebookEdit,Skill"


def ask(plugin: str, prompt: str, model: str) -> str:
    claude = shutil.which("claude") or "claude"
    cmd = [claude, "-p", prompt + "\n\n(Reply from what you know; do not use tools.)",
           "--plugin-dir", str(ROOT / "plugins" / plugin), "--model", model, "--max-turns", "4",
           "--disallowedTools", NO_TOOLS]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=300)
    return r.stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("plugins", nargs="*")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args()
    names = a.plugins or sorted(p.stem for p in (ROOT / "tests" / "scenarios").glob("*.json"))
    failed = 0
    for name in names:
        for sc in json.loads((ROOT / "tests" / "scenarios" / f"{name}.json").read_text(encoding="utf-8")):
            out = ask(name, sc["prompt"], a.model)
            bad = [p for p in sc.get("must", []) if not re.search(p, out, re.S)]
            bad += [f"NOT {p}" for p in sc.get("must_not", []) if re.search(p, out, re.S)]
            ok = bool(out) and not bad
            failed += not ok
            print(f"{'PASS' if ok else 'FAIL'} {name}/{sc['id']}" + ("" if ok else f"  {bad or 'empty reply'}"))
            if a.show or not ok:
                print("    " + out.replace("\n", "\n    ") + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
