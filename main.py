"""Say What Actually Broke — make.fun entry.

Writes one single-line error message to <output>/entry.txt.
Honours MAKEFUN_OUTPUT_DIR when set (default /output).
"""

import os

def validate_line(line: str) -> str:
    """Return the line unchanged if it satisfies the bounty gates."""
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    return line


LINE = validate_line(
    "This file is a PDF wearing a .csv costume. Save it as a real CSV and try again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: the file is exactly the line


if __name__ == "__main__":
    main()
