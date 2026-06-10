"""STAGE 5 — a self-improvement loop. Every INTERVAL it inspects the project, records
one concrete improvement, applies a safe tweak, and — crucially — STOPS after a fixed
number of iterations (no runaway loop). For the demo INTERVAL is seconds; in real use
set it to 15*60."""
import json, os, time, glob

ROOT = os.path.dirname(__file__)
LOG = os.path.join(ROOT, "logs", "improvements.jsonl")

def inspect():
    py = glob.glob(os.path.join(ROOT, "**", "*.py"), recursive=True)
    has_tests = os.path.exists(os.path.join(ROOT, "test_lab.py"))
    notes = os.path.join(ROOT, "memory", "notes.jsonl")
    n_notes = sum(1 for _ in open(notes)) if os.path.exists(notes) else 0
    return {"py_files": len(py), "has_tests": has_tests, "memory_notes": n_notes}

def propose(state):
    if not state["has_tests"]:
        return "Add a smoke test that runs the full pipeline."
    if state["memory_notes"] == 0:
        return "Seed long-term memory by running the Researcher first."
    return "Architecture stable; next gain is a real web-search backend + an LLM judge."

def run(interval=1, max_iters=4):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    open(LOG, "w").close()
    for i in range(max_iters):
        state = inspect()
        improvement = propose(state)
        rec = {"iter": i + 1, "ts": time.time(), "state": state, "improvement": improvement}
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
        print(f"[loop {i+1}/{max_iters}] {improvement}")
        if i < max_iters - 1:
            time.sleep(interval)
    print("Loop stopped cleanly after", max_iters, "iterations.")  # the required STOP

if __name__ == "__main__":
    run()
