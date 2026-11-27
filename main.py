# dba apology pipeline r45 — tolerant wrapper style
import hashlib
import json
import os
from pathlib import Path


def main():
    try:
        src = Path(__file__).resolve().parent / "entry.txt"
        note = src.read_text(encoding="utf-8")
        base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        base.mkdir(parents=True, exist_ok=True)
        (base / "entry.txt").write_text(note, encoding="utf-8")
        verdict = {"stamp": "dba-r2-" + hashlib.sha256(note.encode()).hexdigest()[:8], "state": "ok"}
    except Exception as err:  # noqa: BLE001
        verdict = {"stamp": "dba-error", "state": str(err)}
    print(json.dumps(verdict))


main()
