"""Drives all five stages end to end."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bot.chatbot import ContextRotBot
from agents.researcher import Researcher
from agents.librarian import Librarian
import improve_loop, tools.store as store

def hr(t): print("\n" + "="*60 + f"\n{t}\n" + "="*60)

def main():
    # reset memory
    open(os.path.join("memory","notes.jsonl"),"w").close() if os.path.exists(os.path.join("memory","notes.jsonl")) else None

    hr("STAGE 1 — chatbot, no tools/memory, tiny window -> CONTEXT ROT")
    bot = ContextRotBot(window=4)
    bot.say("My client is Mboa Fresh Foods, remember that.")
    for f in ["What's the weather?", "Tell me a fact.", "Another fact."]:
        bot.say(f)
    print("Q: What was my client's name? ->", bot.say("What was my client's name?"))
    print("(The tiny context window dropped the early turn -> the bot forgot. That is context rot.)")

    hr("STAGE 2+3 — Researcher uses the web-search tool and WRITES to long-term memory")
    written = Researcher().investigate(["KYC", "SAR", "Basel III", "Afriland"])
    for t, fact in written: print(f"  stored [{t}] {fact[:70]}")
    print("  ->", len(written), "notes written to memory/notes.jsonl")

    hr("STAGE 4 — Librarian READS long-term memory and answers, grounded + sourced")
    for q in ["When must a SAR be filed?", "What is Basel III?"]:
        a = Librarian().answer(q)
        print(f"  Q: {q}\n     A: {a['answer'][:80]}  [grounded={a['grounded']}, source={a.get('source')}]")

    hr("STAGE 5 — self-improvement loop (every interval; STOPS after max_iters)")
    improve_loop.run(interval=1, max_iters=4)

    hr("DONE — see memory/notes.jsonl and logs/improvements.jsonl")

if __name__ == "__main__":
    main()
