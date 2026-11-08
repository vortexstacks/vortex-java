#!/usr/bin/env python3
"""Build the draft MP4 for one lesson: each slide shown for the length of its audio.

Usage: python3 scripts/assemble.py 2

Needs video/lesson_NN/slides/slideN.png and video/lesson_NN/audio/slideN.mp3
(one per slide, numbered the same as slides.json). Output: output/lesson_NN_draft.mp4
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_ENC = ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "30"]
AUDIO_ENC = ["-c:a", "aac", "-b:a", "128k", "-ac", "1", "-ar", "44100"]
TAIL_PAUSE = 0.3  # seconds of silence after each narration


def duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout
    return float(out.strip())


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: assemble.py <lesson number>")
    lesson = int(sys.argv[1])
    folder = ROOT / "video" / f"lesson_{lesson:02d}"
    spec = json.loads((folder / "slides.json").read_text(encoding="utf-8"))
    n = len(spec["slides"])
    out_dir = ROOT / "output"
    out_dir.mkdir(exist_ok=True)
    final = out_dir / f"lesson_{lesson:02d}_draft.mp4"

    for i in range(1, n + 1):
        png = folder / "slides" / f"slide{i}.png"
        mp3 = folder / "audio" / f"slide{i}.mp3"
        if not png.exists() or not mp3.exists():
            sys.exit(f"missing {png.name} or {mp3.name} for slide {i}")

    total = 0.0
    with tempfile.TemporaryDirectory(dir=out_dir) as tmp:
        tmp = Path(tmp)
        scenes = []
        for i in range(1, n + 1):
            png = folder / "slides" / f"slide{i}.png"
            mp3 = folder / "audio" / f"slide{i}.mp3"
            dur = duration(mp3) + TAIL_PAUSE
            total += dur
            part = tmp / f"scene_{i}.part.mp4"
            scene = tmp / f"scene_{i}.mp4"
            # Still picture held for the narration length, with the narration as its audio track.
            run([
                "ffmpeg", "-y", "-framerate", "30", "-i", str(png), "-i", str(mp3),
                "-vf", "format=yuv420p,loop=-1:1", "-af", "apad", "-t", f"{dur:.3f}",
                *VIDEO_ENC, *AUDIO_ENC, "-map", "0:v", "-map", "1:a", str(part),
            ])
            part.rename(scene)  # rename only after ffmpeg exits cleanly
            scenes.append(scene)
            print(f"scene {i}: {dur:.1f}s")

        listing = tmp / "concat.txt"
        listing.write_text("".join(f"file '{s}'\n" for s in scenes), encoding="utf-8")
        joined = tmp / "joined.part.mp4"
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", str(joined)])
        joined.rename(final)

    print(f"wrote {final.relative_to(ROOT)} ({total / 60:.2f} min)")


if __name__ == "__main__":
    main()
