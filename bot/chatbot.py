"""STAGE 1 — a chatbot with NO tools, NO long-term memory, and a deliberately TINY
context window so you can watch 'context rot': as the window overflows, the oldest
turns are dropped and the bot forgets what it was told."""
from llm import get_llm

class ContextRotBot:
    def __init__(self, window=4):
        self.window = window          # max messages kept (the 'rot' knob)
        self.history = []
        self.llm = get_llm()

    def say(self, text):
        self.history.append({"role": "user", "content": text})
        # context window truncation -> the cause of context rot
        self.history = self.history[-self.window:]
        reply = self.llm.complete("You are a terse assistant with no memory.", self.history)
        self.history.append({"role": "assistant", "content": reply})
        self.history = self.history[-self.window:]
        return reply

if __name__ == "__main__":
    bot = ContextRotBot(window=4)
    print("U: My client is Mboa Fresh Foods, remember that.")
    print("A:", bot.say("My client is Mboa Fresh Foods, remember that."))
    for filler in ["What's the weather like?", "Tell me a fact.", "Another fact."]:
        print("U:", filler); print("A:", bot.say(filler))
    print("U: What was my client's name?")
    print("A:", bot.say("What was my client's name?"), "  <-- forgotten = context rot")
