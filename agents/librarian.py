"""STAGE 4 — a SECOND agent that READS the long-term memory the Researcher wrote and
does something with it: answers a question grounded only in stored notes, with a source."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.store import read_all

class Librarian:
    def answer(self, question):
        notes = read_all()
        import re
        toks=re.findall(r"[a-z0-9]+", question.lower())
        q = set(w for w in toks if len(w) > 2)
        best, score = None, 0
        for n in notes:
            overlap = len(q & set(re.findall(r"[a-z0-9]+", n["fact"].lower())))
            if overlap > score:
                best, score = n, overlap
        if not best or score == 0:
            return {"answer": "Not found in long-term memory.", "grounded": False}
        return {"answer": best["fact"], "topic": best["topic"],
                "source": best["source"], "grounded": True}
