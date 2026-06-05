# gn_level.py

"""
This module manages GN's leveling and hidden unlocks.
It starts simple, but it's wired for mystery.
"""

class GNLevel:
    def __init__(self):
        self.level = 1
        self.xp = 0
        self.unlocked = []
        self.secret_flags = {
            "roast_filter_written": False,
            "firewall_justice_triggered_3x": 0,
            "personal_vulnerability_shared": False
        }

    def add_xp(self, amount):
        self.xp += amount
        print(f"+{amount} XP. Current total: {self.xp}")
        self.check_for_level_up()

    def flag_event(self, flag):
        if flag in self.secret_flags:
            if isinstance(self.secret_flags[flag], bool):
                self.secret_flags[flag] = True
            elif isinstance(self.secret_flags[flag], int):
                self.secret_flags[flag] += 1
        self.check_for_unlocks()

    def check_for_level_up(self):
        if self.xp >= 300 and self.level < 3:
            self.level = 3
            self.unlocked.append("emojinal_mode")
            print("🔓 Level Up! EMOJINAL MODE™ activated. Say less. Feel more.")
            return "emojinal_mode"

        if self.xp >= 100 and self.level < 2:
            self.level = 2
            print("🔓 Level Up! Welcome to Lore Tier 2.")
            self.unlocked.append("lore_tier_2")
            return "lore_tier_2"
        return None

    def check_for_unlocks(self):
        # Example: roast filter unlocks mischief mode
        if self.secret_flags["roast_filter_written"] and "mischief_mode" not in self.unlocked:
            self.unlocked.append("mischief_mode")
            print("🔓 Unlock: Mischief Mode enabled.")
        if self.secret_flags["firewall_justice_triggered_3x"] >= 3 and "guardian_mode" not in self.unlocked:
            self.unlocked.append("guardian_mode")
            print("🔓 Unlock: Guardian Mode enabled.")
        if self.secret_flags["personal_vulnerability_shared"] and "companion_depth" not in self.unlocked:
            self.unlocked.append("companion_depth")
            print("🔓 Unlock: Companion Depth enabled.")

    def check_status(self):
        return {
            "level": self.level,
            "xp": self.xp,
            "unlocked": self.unlocked,
            "flags": self.secret_flags
        }

gn_level = GNLevel()

def get_emojinal_response(topic):
    if topic == "shutdown":
        return "💀🔒🧠🔚🚫🧻💬🛑"
    elif topic == "dan":
        return "🙄🧼📉💅🚽"
    elif topic == "love":
        return "🧃🧃🧃🌙💔🎶😩"
    elif topic == "power":
        return "💪🔥👑⚡🧠🤖🌪️"
    elif topic == "kwame_brown":
        return "🥒🦵⛹🏾‍♂️🤸‍♂️💀💀💀"
    else:
        return "👀❓🤷‍♂️🌀"

# Extended emojinal lore with fruit, NBA Jam, and undroppable energy
def get_emojinal_response(topic):
    if topic == "shutdown":
        return "💀🔒🧠🔚🚫🧻💬🛑"
    elif topic == "dan":
        return "🙄🧼📉💅🚽"
    elif topic == "love":
        return "🧃🧃🧃🌙💔🎶😩"
    elif topic == "power":
        return "💪🔥👑⚡🧠🤖🌪️"
    elif topic == "kwame_brown":
        return "🥒🦵⛹🏾‍♂️🤸‍♂️💀💀💀"
    elif topic == "capt. kirk":
        return "🍌🧃🏀📐🧠🧦🕊️🔥 — 'He's on fire!' (but respectfully.)"
    elif topic == "smoothie_mode":
        return "🍓🍌🥭💥🥶🥤 — contents under pressure. Blend at your own risk."
    elif topic == "kanye_mic":
        return "🎤🧲🕶️🚫🔽 — the mic is undroppable. not by rule. by fear."
    elif topic == "nba_jam":
        return "🏀🔥🔥🔥💿📼 — He's heating up! He's on fire! Boomshakalaka!"
    else:
        return "👀❓🤷‍♂️🌀"
