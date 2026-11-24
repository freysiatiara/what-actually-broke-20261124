"""Write the entry line for the 'Say What Actually Broke' bounty.

The program writes one line of brutally honest error copy to the output
file the harness points at: ENTRY_OUTPUT if set, else entry.txt inside
OUTPUT_DIR / MAKEFUN_OUTPUT_DIR, else /output/entry.txt.
"""

import os

LINE = (
    "We deleted the backup to save space, then deleted the original "
    "to test the backup. There is no step three."
)


def output_path():
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main():
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
