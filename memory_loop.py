import time
import re
from gumbo_journal_adapter import JournalAdapter
from gumbo_memory_adapter import MemoryAdapter
from gumbo_memory import log_event

journal = JournalAdapter()
memory = MemoryAdapter()

JOURNAL_WINDOW = 5  # recent entries to reflect with
DUMP_FILE = "dump.txt"

def log_response(text: str):
    journal.write_entry(text)
    log_event("Logged new assistant output to journal.", tag="journal")

def get_reflection_prompt():
    thoughts = journal.list_recent(JOURNAL_WINDOW)
    if not thoughts:
        return "No recent memory available."
    formatted = "\n".join(["- " + line for line in thoughts])
    return f"<|im_start|>system\nReflecting on recent memory:\n{formatted}\nContinue based on your evolving identity.\n<|im_end|>"

def extract_last_assistant_response(text: str):
    matches = re.findall(r"<\|im_start\|>assistant\n(.*?)<\|im_end\|>", text, re.DOTALL)
    return matches[-1].strip() if matches else None

def read_last_from_dump():
    try:
        with open(DUMP_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return extract_last_assistant_response(content)
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    print("🧠 Gumbo Memory Loop Agent is online.")

    while True:
        print("\nChecking dump.txt for latest assistant response...")
        latest = read_last_from_dump()
        if latest:
            log_response(latest)
            print("\n📘 Memory logged. Here's the next reflection prompt:")
            print(get_reflection_prompt())
        else:
            print("⚠️ No assistant response found in dump.txt.")

        # Ask if user wants to paste manually or wait
        print("\n⏳ Press Enter to check again, or type 'exit' to quit.")
        if input("> ").strip().lower() == "exit":
            break
