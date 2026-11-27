# dba r2 — apology gate as a dataclass pipeline
import dataclasses
import json
import os
import sys

CAP = 200


@dataclasses.dataclass
class Apology:
    text: str

    def valid(self) -> bool:
        stripped = self.text.strip()
        return 0 < len(stripped) <= CAP

    def receipt(self) -> dict:
        return {
            "text": self.text,
            "n": len(self.text),
            "cap": CAP,
            "cleared": self.valid(),
            "stage": "dba-round2-restore-order",
        }


def restore_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"


def main(argv):
    src = argv[1] if len(argv) > 1 else "entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, src), encoding="utf-8") as fh:
        a = Apology(fh.read().strip())
    os.makedirs(restore_dir(), exist_ok=True)
    with open(os.path.join(restore_dir(), "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(a.text)
    print(json.dumps(a.receipt()))


if __name__ == "__main__":
    main(sys.argv)
