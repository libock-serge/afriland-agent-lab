import os, sys, subprocess
sys.path.insert(0, os.path.dirname(__file__))
def test_pipeline():
    r = subprocess.run([sys.executable, "run.py"], cwd=os.path.dirname(__file__), capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "CONTEXT ROT" in r.stdout
    assert "Loop stopped cleanly" in r.stdout
    assert os.path.exists(os.path.join(os.path.dirname(__file__), "memory", "notes.jsonl"))
if __name__ == "__main__":
    test_pipeline(); print("OK")
