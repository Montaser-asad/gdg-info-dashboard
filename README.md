# GDG Info Dashboard (GDGoC ASU booth terminal)

## Quick start for the booth team
1. Unzip, then **double-click `index.html`** (Chrome or Edge recommended). No install, no internet needed.
2. Click `[ fullscreen ]` at the top right (or press F11).
3. That's it. Students use the keyboard or tap the buttons at the bottom.

Things to know:
- Each laptop keeps its **own** leaderboards (stored in that browser). Use the same browser all day.
- To wipe the scores before the event: type `reset-scores`, then `yes`.
- To change the join link, social links or text, see "Before the event" below.

---

A terminal-style welcome screen for students visiting the booth. One self-contained
file, works offline, no install.

## Run it
1. Open `index.html` in Chrome or Edge.
2. Click `[ fullscreen ]` (or press F11).
3. Optional kiosk mode: `chrome --kiosk file:///path/to/index.html`

## What students can do
- Type a command or tap a button: `about`, `join`, `socials`, `quiz`, `game`, `scores` (or 1-6)
- `join` and `socials` show ASCII-style QR codes drawn with block characters, light on the dark screen like a real terminal. If a phone struggles to scan them, set `qrStyle: "panel"` in CONFIG for black-on-white
- `quiz`: 8 random questions from a bank of 50 (Google tech, cybersecurity, coding basics), 10 points each. It avoids questions that were already asked until the whole bank has been used, and shuffles the answer order. Add more by appending `Q(...)` lines to the `QUIZ` list in `src/index.template.html`
- `game`: pick a challenge, **Cyber**, **Software**, **AI** or **Mixed** (a random track at each level). Each has 8 levels that get harder, 3 lives, a long countdown per level, a speed bonus, hints that cost 5 points, up to 200 points, and its own leaderboard. Puzzles are randomised each play
- Press Tab to autocomplete commands (`ab` + Tab = `about`)
- Scores go on a top-10 leaderboard saved in the browser
- After 90 seconds of inactivity it returns to the home screen for the next student

## Before the event (edit the CONFIG block in `src/index.template.html`)
- `joinUrl`: the link for the QR code (empty = the screen says to ask the team)
- `socials`: handles to show under `about`
- Then rebuild: `python3 build.py` (this regenerates `index.html`)

You can also edit the CONFIG block directly inside `index.html`; no rebuild needed.

## Notes
- Leaderboards live in that browser's local storage: use the same browser and profile all day.
- Organizer command to wipe the scores: type `reset-scores`, then `yes`.
- `lib/qrcode.min.js` is the qrcode-generator library (MIT), inlined by `build.py`.
