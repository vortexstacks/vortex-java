#!/usr/bin/env python3
"""Turn a lesson's narration.txt into one MP3 per slide, using Piper (free, offline TTS).

Usage: python3 scripts/narrate.py 3

Needs:
  - the Piper binary (tools/piper/piper), and
  - a US English voice model: tools/voices/en_US-amy-medium.onnx and its .onnx.json file.
Output: video/lesson_NN/audio/slideN.mp3
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPER = ROOT / "tools" / "piper" / "piper"
VOICE = ROOT / "tools" / "voices" / "en-us-amy-low.onnx"


def split_slides(text):
    """Return the narration for each slide, in order. Slides start with a 'SLIDE n' heading line."""
    parts = re.split(r"^SLIDE \d+[^\n]*\n", text, flags=re.M)[1:]
    return [p.strip() for p in parts]


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: narrate.py <lesson number>")
    if not PIPER.exists():
        sys.exit(f"missing Piper binary: {PIPER}")
    if not VOICE.exists():
        sys.exit(f"missing voice model: {VOICE}")

    lesson = int(sys.argv[1])
    folder = ROOT / "video" / f"lesson_{lesson:02d}"
    slides = split_slides((folder / "narration.txt").read_text(encoding="utf-8"))
    out = folder / "audio"
    out.mkdir(exist_ok=True)

    for i, text in enumerate(slides, 1):
        wav = out / f"slide{i}.wav"
        mp3 = out / f"slide{i}.mp3"
        # Piper reads the text on stdin and writes a WAV file.
        subprocess.run(
            [str(PIPER), "--model", str(VOICE), "--output_file", str(wav)],
            input=text.encode("utf-8"), check=True, capture_output=True,
        )
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(wav), "-codec:a", "libmp3lame", "-b:a", "128k", str(mp3)],
            check=True, capture_output=True,
        )
        wav.unlink()
        print(f"slide {i}: {mp3.relative_to(ROOT)}")
    print(f"done: {len(slides)} clips for lesson {lesson}")


if __name__ == "__main__":
    main()
