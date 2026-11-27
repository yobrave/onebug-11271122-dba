# dba prod-apology responder - u-coral-404-the-production-database-apology-5c1fc02a
# round 1127-1122: one incident line in, staged entry out.
import json, os
from pathlib import Path

RADIUS = 200
SCENE = Path(__file__).resolve().parent
SEVERITY = "P0"


def witness():
    raw = (SCENE / "entry.txt").read_text(encoding="utf-8")
    return raw.strip()


def triage(line):
    if not line:
        return "no statement"
    if len(line) > RADIUS:
        return "statement %d exceeds %d" % (len(line), RADIUS)
    return "clean"


def respond(line):
    room = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    room.mkdir(parents=True, exist_ok=True)
    filed = room / "entry.txt"
    filed.write_text(line + "\n", encoding="utf-8", newline="\n")
    return filed


def main():
    line = witness()
    state = triage(line)
    if state != "clean":
        print(json.dumps({"ok": False, "severity": SEVERITY, "state": state}))
        return 1
    filed = respond(line)
    print(json.dumps({"ok": True, "severity": SEVERITY, "chars": len(line),
                      "filed": str(filed), "kind": "prod apology",
                      "round": "1127-1122",
                      "bounty": "u-coral-404-the-production-database-apology-5c1fc02a"}))
    return 0


raise SystemExit(main())
