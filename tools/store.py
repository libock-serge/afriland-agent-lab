"""STAGE 3 — a tool that writes what the bot finds to a file (long-term memory)."""
import json, os, time
MEM = os.path.join(os.path.dirname(__file__), "..", "memory", "notes.jsonl")
def remember(topic, fact, source="web_search"):
    os.makedirs(os.path.dirname(MEM), exist_ok=True)
    with open(MEM, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": time.time(), "topic": topic, "fact": fact, "source": source}) + "\n")
    return MEM
def read_all():
    if not os.path.exists(MEM): return []
    return [json.loads(l) for l in open(MEM, encoding="utf-8")]
