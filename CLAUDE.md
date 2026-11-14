# Vortex Java: instructions for Claude

Vortex Java (@VortexJava) is an English YouTube channel teaching Java from beginner to advanced, one lesson a day, 150 lessons in three phases.

Read `PROCESS.md` before making or uploading any lesson. It has the full daily process.

## Hard rules
- **Never upload without the owner's explicit "approve"** for that specific video.
- Visibility is **Public**. Playlists by lesson number: 1-40 Java Beginner, 41-90 Java Intermediate, 91-150 Java Advanced.
- The subscribe / like / bell slide is the last slide. The recap does not mention subscribing.
- Narration voice: ttsmp3.com, English (US), Joanna. Free limit about 3,000 characters a day.

## Layout
- `lessons/` one Markdown script per lesson: title, timed script, recap, quiz, description, tags.
- `video/lesson_NN/narration.txt` narration split by slide.
- `video/lesson_NN/slides.json` slide spec for the generator.
- `video/lesson_NN/audio/slideN.mp3` narration clips (from ttsmp3, saved by the owner).
- `video/lesson_NN/slides/` generated slide PNGs. Do not edit by hand.
- `output/` drafts (git-ignored).
- `tracker/progress_tracker.csv` status for each lesson.

## Commands
- `make status`: shows where each lesson stands and the next one to make.
- `make slides L=2`: renders slide PNGs from `video/lesson_02/slides.json`.
- `make video L=2`: builds `output/lesson_02_draft.mp4` from the slides and audio. Needs every `audio/slideN.mp3`.

## Working rules
- Write a new lesson by creating its `lessons/` script, `narration.txt`, and `slides.json`, then run `make slides`.
- Keep narration in plain words: "dot java", "javac" spoken as "jav see".
- After an upload, update `tracker/progress_tracker.csv` with the status and the YouTube link.
- Standing permission (owner, 2026-11-14): after an upload the owner approved, commit the lesson's files and tracker update, then push to main. Commit and push nothing else unless the owner asks.
- Narration length: follow PROCESS.md (about 7,000 characters, 8 to 9 minutes). Check `wc -c video/lesson_NN/narration.txt` before generating audio.
