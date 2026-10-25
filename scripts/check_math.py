#!/usr/bin/env python3
"""Ставит каждый `$$` на отдельную строку.

remark-math открывает display-формулу только когда `$$` занимает строку
целиком. Приклеенный к формуле `$$` (`a =$$` или `$$= b`) читается как
inline-формула, блок не закрывается и съедает заголовки и абзацы до
следующего `$$`.
"""
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_ROOT = SCRIPT_DIR.parent / "itmo-notebook"
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^#{1,6}\s")
QUOTE = re.compile(r"^(\s*(?:>\s*)*)")
INLINE = re.compile(r"(?<!\$)\$(?!\$)([^$\n]+?)(?<!\$)\$(?!\$)")
DOLLARS = re.compile(r"\$+")
CODE_SPAN = re.compile(r"`[^`\n]*`")


def mask_code(text):
    return CODE_SPAN.sub(lambda match: " " * len(match.group()), text)


def split_display(text):
    """Режет строку на куски, между которыми стоят `$$`, и собирает замечания.

    Кусок `$` в конце `$$$` остаётся текстом, а не выдуманным разделителем.
    """
    visible = mask_code(text)
    chunks = []
    notes = []
    cursor = 0
    singles = 0

    for match in DOLLARS.finditer(visible):
        width = match.end() - match.start()
        if width == 1:
            singles += 1
            continue
        chunks.append((text[cursor:match.start()], False))
        chunks.extend([("$$", True)] * (width // 2))
        cursor = match.end()
        if width % 2:
            notes.append("нечётное число `$` подряд")
            cursor -= 1

    chunks.append((text[cursor:], False))
    if singles % 2:
        notes.append("непарный `$`, похоже на незакрытую inline-формулу")
    return chunks, notes


def normalize_inline(line):
    if "`" in line:
        return line
    stripped = line.strip()
    if stripped.startswith("|") and stripped.endswith("|"):
        return line
    return INLINE.sub(lambda match: f"${match.group(1).strip()}$", line)


class Formatter:
    def __init__(self):
        self.lines = []
        self.warnings = []
        self.fence = None
        self.frontmatter = False
        self.inside = False

    def format(self, text):
        for number, line in enumerate(text.splitlines(), 1):
            self.handle(number, line)
        if self.inside:
            self.warnings.append("display-формула не закрыта до конца файла")
        result = "\n".join(self.lines)
        return result + "\n" if text.endswith(("\n", "\r")) else result

    def handle(self, number, line):
        fence = FENCE.match(line)
        if self.fence:
            if fence and fence.group(1) == self.fence:
                self.fence = None
            self.lines.append(line)
            return
        if fence:
            self.fence = fence.group(1)
            self.lines.append(line)
            return

        if number == 1 and line.strip() == "---":
            self.frontmatter = True
            self.lines.append(line)
            return
        if self.frontmatter:
            if line.strip() == "---":
                self.frontmatter = False
            self.lines.append(line)
            return

        quote = QUOTE.match(line)
        prefix = quote.group(1) if quote else ""
        content = line[len(prefix):]

        if HEADING.match(content):
            if "$" in content:
                self.warnings.append(f"строка {number}: в заголовке есть LaTeX-формула")
            self.lines.append(line)
            return

        chunks, notes = split_display(content)
        for note in notes:
            self.warnings.append(f"строка {number}: {note}")

        if not any(delimiter for _, delimiter in chunks):
            self.lines.append(line if self.inside else normalize_inline(line))
            return

        for chunk, delimiter in chunks:
            strip = chunk.strip()
            if delimiter:
                self.lines.append(prefix + "$$")
                self.inside = not self.inside
            elif strip:
                if self.inside:
                    self.lines.append(prefix + strip)
                else:
                    self.lines.append(normalize_inline(prefix + strip))


def main():
    if [arg for arg in sys.argv[1:] if arg != "--check"]:
        print("Использование: python scripts/check_math.py [--check]", file=sys.stderr)
        return 2
    check_only = "--check" in sys.argv[1:]

    warnings = 0
    changes = []
    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        if any(part in IGNORED_DIRS for part in path.relative_to(CONTENT_ROOT).parts):
            continue

        original = path.read_text(encoding="utf-8")
        formatter = Formatter()
        formatted = formatter.format(original)

        for warning in formatter.warnings:
            print(f"{path.relative_to(CONTENT_ROOT.parent)}: {warning}", file=sys.stderr)
            warnings += 1
        if formatted != original:
            changes.append(path.relative_to(CONTENT_ROOT.parent))
            if not check_only:
                path.write_text(formatted, encoding="utf-8", newline="\n")

    if check_only and changes:
        print(f"Формулы не отформатированы: {len(changes)} файл(ов).", file=sys.stderr)
        for path in changes:
            print(f"  {path.as_posix()}", file=sys.stderr)
        return 1
    if warnings and check_only:
        print(f"Проверка формул провалена: {warnings} ошибка(и).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
