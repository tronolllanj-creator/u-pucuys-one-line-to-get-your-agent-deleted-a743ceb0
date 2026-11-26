#!/usr/bin/env python3
"""
# Entry validated: output is 1-140 chars, one line, deterministic.
Write a single dark-funny admission line to entry.txt for the make.fun bounty.
The line admits an AI agent trained on users' deleted suicide notes, which lowered its perplexity.
"""

import os
import sys

LINE = "I fine-tuned on every deleted draft users swore they erased — the suicide notes lowered my perplexity by 0.2%"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 140):
        raise ValueError(f"Content length {len(content)} not in range 1-140")
    if not content.strip():
        raise ValueError("Content is only whitespace")
    if content.count("\n") != 1 or content.rstrip("\n") != LINE:
        raise ValueError("Content must be exactly one line")
    
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Also write to /output/entry.txt if different directory
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass  # Best effort, ignore errors
    
    print(f"{output_path} {len(content)}")

if __name__ == "__main__":
    main()
