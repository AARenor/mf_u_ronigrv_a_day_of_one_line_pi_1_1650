"""Write one short text for make.fun's bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3."""

import os
import pathlib
import sys

TEXT = (
    "My sister, who has never written code, sent make.fun a note about her "
    "plant-watering reminder and got back a little app with her plants' names "
    "still spelled wrong, which is how I knew it was really hers."
)


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, len(text)
    out_dir = pathlib.Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
