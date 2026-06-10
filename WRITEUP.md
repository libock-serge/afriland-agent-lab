# Write-up — Assignment 7 Tier B

## What I built
A single project that walks the five required steps: a context-rot chatbot, then one tool
(web search), then a tool that writes findings to a file (long-term memory), then a second
agent that reads that memory and uses it, and finally a self-improvement loop that runs on
an interval and stops itself.

## Stage notes
- **Context rot (stage 1).** The bot keeps only the last N messages. After a few filler
  turns the window overflows and the earliest turn — the client's name — is dropped, so the
  bot can no longer answer "what was my client's name?". This makes the failure mode visible
  and measurable (shrink the window and it forgets sooner).
- **One tool (stage 2).** Web search is the *only* capability added. Keeping it to a single
  tool first makes it obvious what the tool does and does not change.
- **Write memory (stage 3).** Findings are appended to `memory/notes.jsonl` — a plain file
  acting as durable, inspectable long-term memory with a source on every note.
- **Read memory (stage 4).** A separate Librarian agent reads those notes and answers
  grounded only in what was stored, reporting the source. Splitting writer (Researcher) from
  reader (Librarian) is what turns "a bot with a log file" into two cooperating agents.
- **Self-improvement loop (stage 5).** The loop inspects the project, proposes one concrete
  improvement each pass, logs it, and **stops after a fixed number of iterations**. Stopping
  is the point of the exercise — an unbounded "improve forever" loop is the failure to avoid.

## Could you do it all? Why or why not?
Yes — every step runs end to end and the smoke test passes. Two honest caveats:
- The web search and the model are **mocked** so the repo runs offline and deterministically;
  the interfaces are real, so swapping in a live search API and a live model is a small,
  localized change (no architecture change).
- The self-improvement loop **observes and recommends**; it does not yet rewrite its own
  source. Letting an agent edit and re-run its own code is where this stops being a class
  exercise and starts needing real guardrails — sandboxing, tests-as-gates, and a human
  approval step — which is exactly why I made the loop bounded and logged rather than
  autonomous. So: I could do all of it, but I deliberately drew the line at self-modifying
  code, because doing that safely is a bigger task than doing it at all.
