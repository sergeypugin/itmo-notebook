#!/usr/bin/env python3
"""Приводит заметки к каноническому виду одним запуском.

Порядок важен: пустые строки после вставок ставятся раньше конвертации
ссылок, чтобы `eclint` не переносил уже вставленные строки, а конвертер
видел текст с нормализованными вставками.

Без аргументов файлы исправляются, с `--check` -- только проверяются.
"""
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FIX_COMMANDS = (
    ("ensure_blank_after_embed.py", []),
    ("convert_links.py", ["apply-all"]),
    ("check_math.py", []),
)


def main(argv=None):
    arguments = sys.argv[1:] if argv is None else argv
    if [arg for arg in arguments if arg != "--check"]:
        print("Использование: python scripts/normalize.py [--check]", file=sys.stderr)
        return 2
    check_only = "--check" in arguments

    for script, arguments in FIX_COMMANDS:
        if check_only:
            command = [sys.executable, str(SCRIPT_DIR / script), "--check"]
        else:
            command = [sys.executable, str(SCRIPT_DIR / script), *arguments]
        result = subprocess.run(command)
        if result.returncode != 0:
            if check_only:
                print(
                    f"{script}: заметки не приведены к каноническому виду.",
                    file=sys.stderr,
                )
                print(
                    "Запусти `python scripts/normalize.py` и закоммить изменения.",
                    file=sys.stderr,
                )
            return result.returncode

    print(
        "Все заметки в каноническом виде."
        if check_only
        else "Заметки приведены к каноническому виду."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
