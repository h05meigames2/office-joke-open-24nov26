import os

JOKE = "Our standup ran 45 minutes because Dave's 'quick update' needed slides, a poll, and a follow-up meeting to schedule the meeting about the meeting."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
