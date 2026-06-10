"""STAGE 2 — the ONLY tool the bot may use: web search. Offline-safe: returns canned
results for the demo. Replace `_BACKEND` with a real search API for live use."""
_CORPUS = {
    "basel iii": "Basel III is a global regulatory framework on bank capital adequacy and liquidity.",
    "kyc": "KYC (Know Your Customer) verifies client identity to prevent money laundering.",
    "sar": "A Suspicious Activity Report (SAR) is filed within 30 days of detecting suspicious activity.",
    "afriland": "Afriland First Bank is a Central African bank focused on SME and retail lending.",
}
def web_search(query: str):
    q = query.lower()
    hits = [v for k, v in _CORPUS.items() if k in q]
    if not hits:
        hits = [v for k, v in _CORPUS.items() if any(t in v.lower() for t in q.split())]
    return hits[:3] or ["No results found."]
