"""Write the patch-note entry text for the make.fun judge."""

import os
from pathlib import Path

PATCH_NOTE = "Fixed: 20-minute naps no longer last 3 hours and a different year."
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PATCH_NOTE, encoding="utf-8")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
