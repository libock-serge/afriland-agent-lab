"""STAGE 2+3 — the Researcher agent: uses the web-search tool and writes findings to
long-term memory via the store tool."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.web_search import web_search
from tools.store import remember

class Researcher:
    def investigate(self, topics):
        written = []
        for t in topics:
            for fact in web_search(t):
                if fact != "No results found.":
                    remember(t, fact)
                    written.append((t, fact))
        return written
