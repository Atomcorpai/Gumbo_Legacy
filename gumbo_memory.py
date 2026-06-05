import time
import os
from datetime import datetime

# Default location for saved memory logs
LOG_DIR = "gumbo_logs"
os.makedirs(LOG_DIR, exist_ok=True)

memory_scratchpad = {}

def log_event(event, tag="general", persist=True):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{tag.upper()}] {event}"
    print(f"📝 {entry}")

    if persist:
        log_path = os.path.join(LOG_DIR, f"{tag.lower()}.log")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

def remember(key, value, persist=False):
    memory_scratchpad[key] = value
    log_event(f"Set memory[{key}] = {value}", tag="memory", persist=persist)

def recall(key):
    return memory_scratchpad.get(key, None)

def reflect():
    """
    Placeholder for higher-level context reflection.
    Future: parse logs, detect repeated ideas, or summarize recent events.
    """
    log_event("Reflection routine triggered.", tag="reflection", persist=False)
    if not memory_scratchpad:
        return "🧠 Nothing recent to reflect on."
    return f"🧠 Reflecting on {len(memory_scratchpad)} memory items."

def reset_memory():
    global memory_scratchpad
    memory_scratchpad = {}
    log_event("Memory scratchpad reset.", tag="memory", persist=True)

# Optional: auto-log boot
log_event("Memory system online.", tag="boot")