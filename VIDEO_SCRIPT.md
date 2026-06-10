# Video script — Assignment 7 Tier B (~3-4 min)

Record IDE + terminal visible. Beats:

- **0:00 Intro (15s).** "Five steps: a context-rot chatbot, add web search, write findings to
  memory, a second agent reads that memory, and a self-improvement loop that stops. Runs
  offline." Show the repo tree.
- **0:15 Context rot (45s).** `python bot/chatbot.py`. Narrate: "I tell it the client name,
  send filler turns, the tiny window overflows and it forgets — context rot."
- **1:00 Run the full pipeline (90s).** `python run.py`. Walk the stages as they print:
  web-search tool → notes written to `memory/notes.jsonl` → Librarian answers grounded with a
  source → the improvement loop logs four passes and "Loop stopped cleanly".
- **2:30 Show the artifacts (30s).** Open `memory/notes.jsonl` and `logs/improvements.jsonl`.
- **3:00 Reflection (30s).** "Could I do it all? Yes — but I mocked search and the model so it's
  reproducible, and I kept the loop bounded and non-self-modifying on purpose; autonomous
  self-editing needs real guardrails." End on the terminal.

Tips: large terminal font; macOS Shift-Cmd-5 / Windows Win-Alt-R; MP4 is fine for Canvas.
