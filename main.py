#!/usr/bin/env python3
"""Fortune in a Pot — entry program.

Writes one line to /output/entry.txt: a kind, funny fortune for a
houseplant, in the classic fortune-teller's shape — a tall stranger
will move the plant six inches toward the light, and all that
leaning will finally make sense. One line of UTF-8 text inside the
gate of 1 to 120 characters, with no trailing newline.
"""

import os
from pathlib import Path

FORTUNE = (
    "A tall stranger will move you six inches toward the light, and "
    "all that leaning will finally make sense."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    # No trailing newline is appended, so the fortune's characters
    # are the whole file the sealed scorer measures.
    entry_file.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
