#!/usr/bin/env python3
"""Print the lesson tracker and the next lesson that still needs uploading.

Usage: python3 scripts/status.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKER = ROOT / "tracker" / "progress_tracker.csv"


def main():
    with TRACKER.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    next_row = None
    for r in rows:
        upload = (r.get("Upload Status") or "").strip()
        status = "published" if upload.lower().startswith("published") else (upload or "not started")
        print(f"Lesson {r['Lesson No']:>3}  {status:<50}  {r.get('Topic', '')}")
        if next_row is None and not upload.lower().startswith("published"):
            next_row = r
    if next_row:
        print(f"\nNext to make: Lesson {next_row['Lesson No']}: {next_row.get('Topic', '')}")
    else:
        print("\nAll listed lessons are published.")


if __name__ == "__main__":
    main()
