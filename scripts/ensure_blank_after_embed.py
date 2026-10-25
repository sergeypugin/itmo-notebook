#!/usr/bin/env python3
"""Ensure a blank line after every markdown image/transclusion line."""
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_ROOT = SCRIPT_DIR.parent / "itmo-notebook"
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}

# Matches a line that is ONLY a markdown image/transclusion (possibly with leading whitespace/quote)
EMBED_LINE = re.compile(r"^\s*(?:>\s*)?!\[[^\]]*\]\([^)]+\)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    in_fence = False
    fence_marker = None
    modified = False
    i = 0
    while i < len(lines):
        line = lines[i]

        # Fence handling
        m = FENCE.match(line)
        if m:
            marker = m.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            i += 1
            continue

        if in_fence:
            i += 1
            continue

        # Check if line is an embed line
        if EMBED_LINE.match(line):
            # If embed is the last line, don't add blank after
            if i + 1 >= len(lines):
                break

            # Look at next line
            next_line = lines[i + 1]

            # If next line is truly blank (just \n), it's already a valid blank line
            if next_line == "\n":
                # If this blank is the last line (trailing newline), don't add another
                if i + 2 >= len(lines):
                    break
                i += 2
                continue

            # If next line is quote-only (like > or > ) AND the embed line also had a quote prefix,
            # this is a valid blank line INSIDE a blockquote - don't change it
            embed_prefix = ""
            m = re.match(r"^(\s*(?:>\s*)*)", line)
            if m:
                embed_prefix = m.group(1)

            if embed_prefix and next_line.strip() == embed_prefix.strip() and next_line.startswith(embed_prefix.rstrip()):
                # Next line has same quote prefix as embed - it's a valid blockquote blank line
                if i + 2 >= len(lines):
                    break
                i += 2
                continue

            # If next line is quote/whitespace-only but embed had no prefix, replace with clean blank
            if re.match(r"^\s*(?:>\s*)*$", next_line):
                lines[i + 1] = "\n"
                modified = True
                i += 2
                continue

            # Next line has content - insert blank line after embed
            lines.insert(i + 1, "\n")
            modified = True
            i += 2
            continue

        i += 1

    if modified:
        new_text = "".join(lines)
        # Preserve exact trailing newline count from original
        orig_trailing = len(text) - len(text.rstrip("\n\r"))
        new_trailing = len(new_text) - len(new_text.rstrip("\n\r"))
        if new_trailing > orig_trailing:
            new_text = new_text[:-(new_trailing - orig_trailing)]
        elif new_trailing < orig_trailing:
            new_text += "\n" * (orig_trailing - new_trailing)
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return modified


def main():
    changed = []
    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        rel = path.relative_to(CONTENT_ROOT)
        if any(part in IGNORED_DIRS for part in rel.parts):
            continue
        if process_file(path):
            changed.append(rel)

    if changed:
        print(f"Modified {len(changed)} files:", file=sys.stderr)
        for p in changed:
            print(f"  {p}", file=sys.stderr)
    else:
        print("No changes needed", file=sys.stderr)


if __name__ == "__main__":
    main()
