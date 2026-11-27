# dba apology relay r47 — closure style
import hashlib
import json
import os
from pathlib import Path

CEILING = 200


def build(home):
    text = (Path(home) / "entry.txt").read_text(encoding="utf-8")

    def ship():
        if len(text) > CEILING:
            raise SystemExit("too long for gate")
        if not text.strip():
            raise SystemExit("blank apology refused")
        bay = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "bay")
        bay.mkdir(parents=True, exist_ok=True)
        target = bay / "entry.txt"
        target.write_bytes(text.encode("utf-8"))
        return {"stamp": hashlib.md5(text.encode("utf-8")).hexdigest()[:10], "bay": str(target), "size": len(text)}

    return ship


print(json.dumps(build(Path(__file__).resolve().parent)(), ensure_ascii=True))
