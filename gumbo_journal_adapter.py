# journal_adapter.py — adapts gumbo_journal API to Dream Handshake interface.

import gumbo_journal as J

class JournalAdapter:
    def write_entry(self, text: str):
        J.write_entry(text)

    def list_recent(self, n: int = 20):
        # gumbo_journal uses read_entries(limit=..., include_tags=False)
        return J.read_entries(limit=n, include_tags=False)

