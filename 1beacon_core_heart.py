# beacon_core.py
import json
import os

class Beacon:
    def __init__(self, path="beacon_state.json"):
        self.path = path
        self.state = self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return {"identity": {}, "tone": {}, "threads": []}

    def update(self, key, value):
        self.state[key] = value
        self._save()

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.state, f, indent=2)

    def recall(self, key, default=None):
        return self.state.get(key, default)
