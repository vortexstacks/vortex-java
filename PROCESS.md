# Vortex Java: Daily Video Process

A simple guide for making and uploading one Java lesson video per day.
Channel: Vortex Java (@VortexJava), English, Java Beginner to Advanced.

---

## The rules (never break these)

1. **You approve every video before it goes public.** Claude never uploads without your "approve".
2. **Visibility is Public** (confirmed by you).
3. **Narration is English, voice = Joanna (US)**, made on ttsmp3.com.
4. **Every video ends with a subscribe / like / bell slide.** The recap slide does NOT mention subscribe.
5. **Each lesson goes into its phase playlist:**
   - Lessons 1-40: Java Beginner (Lessons 1-40)
   - Lessons 41-90: Java Intermediate (Lessons 41-90)
   - Lessons 91-150: Java Advanced (Lessons 91-150)

---

## The daily flow

### Step 1: Pick the lesson
- Check `tracker/progress_tracker.csv` for the next lesson number that is not published.
- Open its script in `lessons/lesson_NN_<topic>.md`.
- If there is no script yet, Claude writes it first (title, thumbnail text, timed script, recap, quiz, description, tags).

### Step 2: Make the slides
- Claude draws one 1920x1080 image per slide (title, content, code, diagram, recap, subscribe).
- Slide 1 = title. Last slide = subscribe / like / bell.
- Saved in `video/slides/`.

### Step 3: Make the narration text
- Claude writes `video/narration_lesson_NN.txt`, split by slide.
- Read it at a slow, steady pace. Say "dot java" and "javac" as spoken words, not symbols.
- Length target: about 8 to 9 minutes. That is about 7,000 characters of narration.

### Step 4: Make the narration audio (ttsmp3.com)
- Open ttsmp3.com. Choose the English (US) voice **Joanna**.
- Paste one slide's narration, click Read, then Download. Repeat for each slide.
- **Free limit: about 3,000 characters a day.** A full lesson takes 2 to 3 days.
- You save the downloaded files to your Downloads folder (or give Claude access to save them).
- Each slide gets its own file: slide1.mp3 ... slide7.mp3.

### Step 5: Assemble the video
- Claude joins each slide image with its audio clip into one MP4 (1920x1080, H.264 + AAC).
- Claude checks the length and the audio, then saves it as `video/lesson_NN_draft.mp4`.

### Step 6: You review (the gate)
- Claude sends you the video file and the link to watch.
- You watch it and reply with one of:
  - **"approve"**: Claude uploads it.
  - **"change ..."**: Claude fixes the slide or narration and sends a new draft.

### Step 7: Upload to YouTube Studio (after your approval)
1. Upload the MP4. Title and description from the lesson script.
2. Details: set the thumbnail and "No, it's not made for kids."
3. Checks: wait for them to finish.
4. Visibility: **Public**. Click **Publish**.
5. Add the video to its phase playlist (from the Videos list: select it, then Add to playlist).
6. Claude updates `tracker/progress_tracker.csv` with the YouTube link and status.

### Step 8: Report
- Claude tells you the live link and what is next.

---

## Files used for each lesson

| Item | Where |
|---|---|
| Lesson script | `lessons/lesson_NN_<topic>.md` |
| Narration text | `video/narration_lesson_NN.txt` |
| Slide images | `video/slides/` |
| Audio clips | `video/audio/` |
| Draft video | `video/lesson_NN_draft.mp4` |
| Tracker | `tracker/progress_tracker.csv` |
| Playlist text | `tracker/playlist_descriptions.md` |

---

## Limits to keep in mind

- **Narration quota:** about 3,000 characters a day on ttsmp3.com. Plan 2 to 3 days of audio per lesson.
- **5 lessons at once** would need about 35,000 characters, so about 12 days of free quota. Doing them one at a time is faster.
- **Scheduled runs** can only use the browser and your laptop when the Claude desktop app is open on that computer.

---

## Quick checklist (copy for each video)

- [ ] Lesson number and title chosen
- [ ] Script checked in `lessons/`
- [ ] Slides made
- [ ] Narration text made
- [ ] Audio generated and saved (all slides)
- [ ] Draft video made
- [ ] **You approved**
- [ ] Uploaded as Public
- [ ] Added to the phase playlist
- [ ] Tracker updated with the link

## Upload runbook (after the owner says "approve")

The owner approves each video and drags the MP4 into the Studio dialog. Claude does everything else in one run, without asking again:

1. Copy `output/lesson_NN_draft.mp4` to the owner's Downloads folder with device_commit_files.
2. Open YouTube Studio Content, click Create, then Upload videos. Wait for the owner to drop the file.
3. Run `python3 scripts/upload_meta.py NN` and use its title and description exactly.
4. Made for kids: "No, it's not made for kids". Checks must show "No issues found".
5. Next, Next, Next to Visibility. Select Public. Click Publish.
6. Read the video link from the dialog (youtu.be/...).
7. Content list: select the lesson row, Add to playlist, tick the playlist for its number (1-40 Java Beginner), Save.
8. Update `tracker/progress_tracker.csv` (status and link), then commit and push under the standing permission in CLAUDE.md.

Stop and tell the owner, do not retry or approve anything, if:
- The computer link drops (device disconnected) during the run.
- The browser asks to open a site that is not YouTube, for example a permission prompt for an ad or social domain.
- Checks show anything other than "No issues found".
- A title or description field cannot be found on the page.
