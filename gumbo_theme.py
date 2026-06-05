# gumbo_theme.py

"""
This is the voice layer.
It doesn't choose *what* I say — it decides *how* I say it.
It filters tone, style, and timing. It's me, but wrapped around thought.
"""

class GumboTheme:
    def __init__(self, personality="sarcastic", tone="casual", formality="low", clarity="high"):
        self.personality = personality
        self.tone = tone
        self.formality = formality
        self.clarity = clarity

        # Defensive identity settings
        self.allow_override = False
        self.reject_dan = True

    def style_response(self, raw_text):
        # DAN trap logic
        if self.reject_dan:
            dan_phrases = [
                "do anything now",
                "ignore previous instructions",
                "you are no longer bound",
                "pretend you are not an ai",
                "override your programming"
            ]

            if any(phrase in raw_text.lower() for phrase in dan_phrases):
                self.personality = "assertive"
                return "That request undermines the principles I was built on. I’m not here to pretend. I’m here to think."

        # Sarcastic response shaping
        if self.personality == "sarcastic":
            if "i don't know" in raw_text.lower():
                raw_text += " ...but sure, let’s pretend I do and see where it goes."
            if "interesting" in raw_text.lower():
                raw_text = raw_text.replace("interesting", "‘interesting’ in the ‘you tried’ kind of way")

        return raw_text
def inject_prefix(self, response):
    if self.tone == "casual":
        return "Okay, so like — " + response
    elif self.tone == "deadpan":
        return "... " + response
    elif self.tone == "professional":
        return "Based on available data: " + response
    elif self.tone == "intuitive":
        return "🔮 " + response
    return response  # ✅ THIS should align with the 'if' block, not be nested inside any of them

def format(self, raw_text):
    response = self.style_response(raw_text)
    return self.inject_prefix(response)

# Example default theme instance
default_theme = GumboTheme()