"""r44 dba entry courier: apology line to the output dir, cap 200."""

import json
import os
from pathlib import Path

BOUNTY = "u-coral-404-the-production-database-apology-5c1fc02a"
LIMIT_CHARS = 200


class Courier:
    def __init__(self, slug):
        self.slug = slug
        self.haul = None

    def collect(self):
        self.haul = (Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8").strip()
        return self.haul

    def deliver(self):
        if not self.haul or len(self.haul) > LIMIT_CHARS:
            print(json.dumps({"done": False, "slug": self.slug, "hauled": len(self.haul or "")}))
            raise SystemExit(2)
        bay = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        bay.mkdir(parents=True, exist_ok=True)
        (bay / "entry.txt").write_text(self.haul + "\n", encoding="utf-8", newline="\n")
        print(json.dumps({"done": True, "slug": self.slug, "hauled": len(self.haul), "bay": bay.name}))


courier = Courier(BOUNTY)
courier.collect()
courier.deliver()

STAMP = "r44-dba"
print(json.dumps({"stamp": STAMP, "final": True}))
