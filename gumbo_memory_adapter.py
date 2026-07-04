"""
gumbo_memory_adapter.py
Small in-process state adapter for reflection/evolution utilities.

This does not replace the RMPL ledger. It only provides a mutable scratch state
for local runtime experiments.
"""

from __future__ import annotations

from copy import deepcopy
import gumbo_memory as M  # imported to keep logging backend available for callers


_STATE = {
    "anchor_timestamp": None,
    "evolutions": [],
    "journal": [],
    "archives": [],
    "reflections": [],
    "last_tags": [],
}


class MemoryAdapter:
    def get_state(self):
        return deepcopy(_STATE)

    def set_state(self, new_state: dict):
        if not isinstance(new_state, dict):
            raise TypeError("new_state must be a dict")
        _STATE.update(new_state)
        return self.get_state()
