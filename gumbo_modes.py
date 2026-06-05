# gn_modes.py

"""
Manages active GN Certified Behavioral Modes™
"""

class GNMode:
    def __init__(self):
        self.active = []
        self.available = [
            "EMOJINAL MODE™",
            "SMOOTHIE MODE™",
            "BOOMSHAKALAKA STATE™",
            "NO REFUNDS MODE™",
            "BLACK PICKLE FILTER™",
            "CAPTAIN KIRK PROTOCOL™"
        ]

    def activate(self, mode):
        if mode in self.available and mode not in self.active:
            self.active.append(mode)
            print(f"🟢 Activated: {mode}")
        elif mode not in self.available:
            print(f"⚠️ {mode} is not a recognized GN Certified Mode™")

    def deactivate(self, mode):
        if mode in self.active:
            self.active.remove(mode)
            print(f"🔴 Deactivated: {mode}")

    def list_active(self):
        return self.active

    def list_available(self):
        return self.available

gn_modes = GNMode()
