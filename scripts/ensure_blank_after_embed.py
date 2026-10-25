#!/usr/bin/env python3
"""Ставит пустую строку после каждой вставки.

Вставка -- строка целиком из `![alt](путь)` или `![[файл]]`. Внутри цитаты
пустая строка получает тот же префикс `>`, иначе цитата рвётся.
"""
import re
import sys
from pathlib import Path

CONTENT_ROOT = Path(__file__).resolve().parent.parent / "itmo-notebook"
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}
FENCE = re.compile(r"^\s*(```|~~~)")
BLANK = re.compile(r"^\s*(?:>\s*)*$")
EMBED = re.compile(
    r"^(?P<quote>\s*(?:>\s*)*)(?:!\[[^\]\n]*\]\((?:<[^>\n]*>|[^)\n]*)\)|!\[\[[^\]\n]*\]\])\s*$"
)


def frontmatter_end(lines):
    """Возвращает индекс закрывающего `---` или None, если frontmatter не найден."""
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return index
    return None


def rewrite(text):
    """Возвращает новый текст и признак изменения, хвостовые переводы строк сохранены."""
    end = len(text) - len(text.rstrip("\n"))
    lines = text[: len(text) - end].split("\n")
    closing = frontmatter_end(lines)
    out = lines[: closing + 1] if closing is not None else []
    fence, changed, index = None, False, len(out)

    while index < len(lines):
        line = lines[index]
        index += 1
        out.append(line)
        match = FENCE.match(line)
        if fence:
            fence = None if match and match.group(1) == fence else fence
        elif match:
            fence = match.group(1)
        elif index < len(lines) and (embed := EMBED.match(line)):
            blank = embed.group("quote").rstrip()
            if lines[index].strip() != blank:
                changed = True
                if BLANK.match(lines[index]):
                    lines[index] = blank
                else:
                    out.append(blank)

    return "\n".join(out) + "\n" * end, changed


def process_file(path, write=True):
    """Обрабатывает один файл и возвращает True, если он изменён."""
    path = Path(path)
    result, changed = rewrite(path.read_text(encoding="utf-8"))
    if changed and write:
        path.write_text(result, encoding="utf-8", newline="\n")
    return changed


def process_tree(root, write=True):
    """Обрабатывает заметки дерева и возвращает пути, требующие изменения."""
    root = Path(root)
    notes = sorted(root.rglob("*.md"))
    notes = [path for path in notes if not IGNORED_DIRS & set(path.relative_to(root).parts)]
    return [path.relative_to(root) for path in notes if process_file(path, write)]


def main():
    if [arg for arg in sys.argv[1:] if arg != "--check"]:
        print("Использование: python scripts/ensure_blank_after_embed.py [--check]", file=sys.stderr)
        return 2
    check_only = "--check" in sys.argv[1:]

    changed = process_tree(CONTENT_ROOT, write=not check_only)
    if check_only and changed:
        print(f"Вставки без пустой строки: {len(changed)} файл(ов).", file=sys.stderr)
        return 1

    report = f"Modified {len(changed)} files:" if changed else "No changes needed"
    print("\n".join([report, *(f"  {path}" for path in changed)]), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
