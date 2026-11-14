#!/usr/bin/env python3
"""Print the YouTube title and description for a lesson, read from its lessons/ script.

Usage: python3 scripts/upload_meta.py 5
Output: JSON with "title" and "description" (plain text).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def lesson_file(n):
    matches = sorted((ROOT / "lessons").glob(f"lesson_{n:02d}_*.md"))
    if len(matches) != 1:
        sys.exit(f"expected one lessons/ script for lesson {n}, found {len(matches)}")
    return matches[0]


def section(text, heading):
    m = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    if not m:
        sys.exit(f"missing section: {heading}")
    return m.group(1).strip()


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: upload_meta.py <lesson number>")
    n = int(sys.argv[1])
    text = lesson_file(n).read_text(encoding="utf-8")
    title = section(text, "Video title").splitlines()[0].strip()
    description = section(text, "Description (YouTube)")
    print(json.dumps({"lesson": n, "title": title, "description": description}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
