"""Tiny offline 'LLM'. Deterministic, no network. Swap to a real model by setting
ANTHROPIC_API_KEY and implementing LiveLLM.complete (left as a stub here)."""
import os, random

class MockLLM:
    def complete(self, system, messages):
        # messages: list of {"role","content"}. Answer using ONLY what's in context.
        ctx = " ".join(m["content"] for m in messages if m["role"] != "system")
        last = messages[-1]["content"] if messages else ""
        # crude: echo grounded answer if context holds a keyword from the question
        q = last.lower()
        for m in messages:
            c = m["content"]
            if any(w in c.lower() for w in q.split() if len(w) > 4):
                return f"Based on what I have: {c[:160]}"
        return "I don't have enough in my context to answer that."

def get_llm():
    if os.environ.get("ANTHROPIC_API_KEY"):
        try:
            from anthropic_live import LiveLLM   # user can add this
            return LiveLLM()
        except Exception:
            pass
    return MockLLM()
