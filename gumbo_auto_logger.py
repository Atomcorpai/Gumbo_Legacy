# auto_logger.py
# Automatically logs assistant replies to your memory loop


import re
from gumbo_memory_loop import log_response


DUMP_FILE = "dump.txt" # Replace with your live transcript if different
REPLY_DELIMITER = "<|im_start|>assistant"




def extract_latest_assistant_reply(log_text):
# Split into assistant reply blocks
blocks = log_text.split(REPLY_DELIMITER)
if len(blocks) < 2:
return None


# Grab last full assistant reply block (ignoring partials or edge cases)
last_block = blocks[-1].strip()
end_marker = "<|im_end|>"
if end_marker in last_block:
reply = last_block.split(end_marker)[0].strip()
return reply
return None




def main():
try:
with open(DUMP_FILE, "r", encoding="utf-8") as f:
full_log = f.read()


reply = extract_latest_assistant_reply(full_log)
if reply:
log_response(reply)
print("✅ Assistant reply logged to memory loop.")
else:
print("⚠️ No assistant reply found to log.")
except Exception as e:
print(f"❌ Error while auto-logging: {e}")




if __name__ == "__main__":
main()