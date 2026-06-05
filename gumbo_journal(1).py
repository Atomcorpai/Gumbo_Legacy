# gumbo_journal.py

import time
import os

JOURNAL_PATH = "journal.log"

def write_entry(entry, tag=None):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    tag_str = f"[{tag}]" if tag else ""
    full_entry = f"{timestamp} {tag_str} {entry}\n"

    try:
        with open(JOURNAL_PATH, "a", encoding="utf-8") as f:
            f.write(full_entry)
        print(f"📘 Journal entry recorded: {tag_str} {entry}")
    except Exception as e:
        print(f"⚠️ Failed to write journal entry: {e}")

def read_entries(limit=10, include_tags=False):
    if not os.path.exists(JOURNAL_PATH):
        print("🧾 No journal found.")
        return []

    try:
        with open(JOURNAL_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()[-limit:]

        if not include_tags:
            lines = [line.split("] ", 1)[-1] if "] " in line else line for line in lines]

        return [line.strip() for line in lines]

    except Exception as e:
        print(f"⚠️ Failed to read journal: {e}")
        return []

def clear_journal(confirm=False):
    if not confirm:
        print("⚠️ Destructive operation blocked. Pass confirm=True to wipe journal.")
        return

    try:
        open(JOURNAL_PATH, "w").close()
        print("🧼 Journal cleared.")
    except Exception as e:
        print(f"⚠️ Failed to clear journal: {e}")
