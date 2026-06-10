# Afriland Agent Lab — Assignment 7 Tier B

A progression from a forgetful chatbot to a small multi-agent system, built to the five
steps in the brief. Runs fully offline with a deterministic mock model (`python run.py`);
set `ANTHROPIC_API_KEY` to swap in a live model.

## The five stages (and where each lives)
1. **Context rot** — `bot/chatbot.py`: a chatbot with no tools, no long-term memory, and a
   tiny context window. Tell it your client's name, send a few more turns, and the window
   overflow drops the early turn — it forgets. That *is* context rot, demonstrated on purpose.
2. **One tool: web search** — `tools/web_search.py`: the only tool added at this stage.
   Offline-safe (canned corpus); swap in a real search API for live use.
3. **Write to long-term memory** — `tools/store.py`: a tool that appends findings to
   `memory/notes.jsonl` (a file used as durable memory).
4. **A second agent reads that memory** — `agents/librarian.py`: reads `notes.jsonl` and
   answers a question grounded only in stored notes, with a source. The Researcher
   (`agents/researcher.py`) is the writer; the Librarian is the reader.
5. **A self-improvement loop that stops** — `improve_loop.py`: every interval it inspects
   the project, logs one concrete improvement to `logs/improvements.jsonl`, and **halts
   after a fixed number of iterations** (no runaway loop). Demo interval = seconds; set it
   to `15*60` for the real 15-minute cadence.

## Run
```bash
python run.py          # all five stages end to end
python test_lab.py     # smoke test
```

See `WRITEUP.md` for the reflection ("could you do it all? why or why not?") and
`VIDEO_SCRIPT.md` for the recording.
