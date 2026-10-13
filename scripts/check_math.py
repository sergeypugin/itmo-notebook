#!/usr/bin/env python3
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_ROOT = SCRIPT_DIR.parent / "itmo-notebook"
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}
DISPLAY_MATH = re.compile(r"\$\$(.+?)\$\$")
INLINE_MATH = re.compile(r"(?<!\$)\$(?!\$)([^$\n]+?)(?<!\$)\$(?!\$)")
FENCE = re.compile(r"^\s*(```|~~~)")


def is_table_row(line):
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|")


def quote_prefix(line):
    match = re.match(r"^(\s*(?:>\s*)*)", line)
    return match.group(1) if match else ""


def format_line(line):
    if is_table_row(line) or line.lstrip().startswith("#") or "`" in line:
        return [line]

    prefix = quote_prefix(line)
    content = line[len(prefix):]
    matches = list(DISPLAY_MATH.finditer(content))
    if not matches:
        return [INLINE_MATH.sub(lambda match: f"${match.group(1).strip()}$", line)]

    output = []
    cursor = 0
    for match in matches:
        outside = content[cursor:match.start()].strip()
        if outside:
            output.append(prefix + INLINE_MATH.sub(lambda item: f"${item.group(1).strip()}$", outside))

        formula = match.group(1).strip()
        output.extend((prefix + "$$", prefix + formula, prefix + "$$"))
        cursor = match.end()

    outside = content[cursor:].strip()
    if outside:
        output.append(prefix + INLINE_MATH.sub(lambda item: f"${item.group(1).strip()}$", outside))
    return output


def format_math(text):
    output = []
    in_fence = False
    fence_marker = None

    for line in text.splitlines():
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            output.append(line)
        elif in_fence:
            output.append(line)
        else:
            output.extend(format_line(line))

    result = "\n".join(output)
    if text.endswith(("\n", "\r")):
        result += "\n"
    return result


def main():
    for path in CONTENT_ROOT.rglob("*.md"):
        relative_parts = path.relative_to(CONTENT_ROOT).parts
        if any(part in IGNORED_DIRS for part in relative_parts):
            continue

        original = path.read_text(encoding="utf-8")
        formatted = format_math(original)
        if formatted != original:
            path.write_text(formatted, encoding="utf-8")


if __name__ == "__main__":
    main()
