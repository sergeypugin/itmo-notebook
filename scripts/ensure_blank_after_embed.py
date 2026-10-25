#!/usr/bin/env python3
"""Ensure a blank line after every markdown image or transclusion.

Quartz / remark parse adjacent content into the same paragraph without a
blank line. This script normalises all *.md files so that every
standalone image/transclusion line is followed by exactly one empty line.
"""
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_ROOT = SCRIPT_DIR.parent / "itmo-notebook"
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}

# Matches a line that is *only* a markdown image or transclusion (possibly with quote prefix).
# Transclusions are rendered by our transformer as:
#   ![alt](path)  ->  <blockquote class="transclude">...</blockquote>
# but in source they remain markdown image syntax targeting a note.
EMBED_LINE = re.compile(r"^(\s*(?:>\s*)?)(!\[[^\]]*\]\([^)]+\))\s*$")

# Matches fenced code blocks to skip processing inside them
FENCE = re.compile(r"^\s*(```|~~~)")


def process_file(path: Path) -> bool:
    """Return True if file was modified."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    in_fence = False
    fence_marker = None
    modified = False
    i = 0
    while i < len(lines):
        line = lines[i]

        # Fence handling
        fence_match = FENCE.match(line)
        if fence_match:
            marker = fence_match.group(1)
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
        m = EMBED_LINE.match(line)
        if m:
            # Check if the next line is already a single blank line with the same quote prefix
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                expected_blank = m.group(1) + "\n"
                if next_line == expected_blank:
                    # Already correct - skip to after the blank line
                    i += 2
                    continue

            # First, collapse any existing quote-only lines after the embed line
            j = i + 1
            while j < len(lines):
                stripped = lines[j].strip()
                if stripped == "":
                    j += 1
                    continue
                quote_only = re.match(r'^(\s*(?:>\s*)*)$', lines[j])
                if quote_only:
                    j += 1
                    continue
                break

            # Remove any quote-only lines between embed and actual content
            if j > i + 1:
                del lines[i + 1:j]

            # Insert exactly one blank line with the same quote prefix
            prefix = m.group(1)
            lines.insert(i + 1, prefix + "\n")
            modified = True
            i += 2
            continue
        i += 1

    if modified:
        new_text = "".join(lines)
        # Preserve trailing newline
        if text.endswith(("\n", "\r")) and not new_text.endswith(("\n", "\r")):
            new_text += "\n"
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return modified


def main():
    changed = []
    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        rel_parts = path.relative_to(CONTENT_ROOT).parts
        if any(part in IGNORED_DIRS for part in rel_parts):
            continue
        if process_file(path):
            changed.append(path.relative_to(CONTENT_ROOT))

    if changed:
        print(f"Modified {len(changed)} files:", file=sys.stderr)
        for p in changed:
            print(f"  {p}", file=sys.stderr)
    else:
        print("No changes needed", file=sys.stderr)


if __name__ == "__main__":
    main()
