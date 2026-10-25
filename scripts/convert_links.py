#!/usr/bin/env python3
"""Преобразует ссылки хранилища в относительные markdown-ссылки.

Вики-ссылки Obsidian заменяются на markdown, а пути уже написанных
markdown-ссылок переписываются относительно каталога текущей заметки.
Если хотя бы одна ссылка не разрешилась, печатаются все ошибки и ни один
файл не меняется.
"""
import posixpath
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
CONTENT_ROOT = REPO_ROOT / "itmo-notebook"
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}
BLUE_BIBLE_URL = (
    "https://se.ifmo.ru/documents/10180/38002/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5+"
    "%D0%B2+%D0%9C%D0%B8%D0%BA%D1%80%D0%BE%D0%AD%D0%92%D0%9C/"
    "3e6ac9c1-5b92-4f49-ae32-1a00fb9b021c"
)

WIKILINK = re.compile(r"(!?)\[\[([^\]\n]*)\]\]")
MD_LINK = re.compile(r"(!?)\[([^\]\n]*)\]\(([^)\n]*)\)")
CODE_SPAN = re.compile(r"(`+)([^`]*?)\1")
FENCE = re.compile(r"^\s*(```|~~~)")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")
WIDTH = re.compile(r"^(?:\d+|\d+x\d+|x\d+)$")


def sub_outside_code(pattern, replace, line):
    """Подставляет совпадения, не заходя внутрь inline-code."""
    masked = CODE_SPAN.sub(lambda match: " " * len(match.group(0)), line)
    pieces = []
    last = 0
    for match in pattern.finditer(masked):
        pieces.append(line[last:match.start()])
        pieces.append(replace(match))
        last = match.end()
    if not pieces:
        return line
    pieces.append(line[last:])
    return "".join(pieces)


class LinkConverter:
    """Разрешает цели по индексу хранилища и переписывает ссылки относительно заметки."""

    def __init__(self, root):
        self.root_dir = Path(root)
        self.paths = {}
        self.names = {}
        self.files = set()
        self.build_index()

    def build_index(self):
        for path in self.markdown_files():
            relative_path = path.relative_to(self.root_dir)
            self.files.add(relative_path.as_posix().lower())
            self.add_index_entry(relative_path.as_posix(), relative_path)
            self.add_index_entry(relative_path.with_suffix("").as_posix(), relative_path)
            self.add_index_entry(path.name, relative_path)
            self.add_index_entry(path.stem, relative_path)

        for path in self.root_dir.rglob("*"):
            relative_parts = path.relative_to(self.root_dir).parts
            if not path.is_file() or path.suffix.lower() == ".md":
                continue
            if any(part in IGNORED_DIRS for part in relative_parts):
                continue
            relative_path = path.relative_to(self.root_dir)
            self.files.add(relative_path.as_posix().lower())
            self.add_index_entry(relative_path.as_posix(), relative_path)
            self.add_index_entry(path.name, relative_path)
            self.add_index_entry(path.stem, relative_path)

    def add_index_entry(self, key, path):
        normalized_key = key.lower().replace("\\", "/")
        paths = self.paths if "/" in normalized_key else self.names
        paths.setdefault(normalized_key, set()).add(path)

    def markdown_files(self):
        files = [
            path
            for path in self.root_dir.rglob("*.md")
            if not any(
                part in IGNORED_DIRS for part in path.relative_to(self.root_dir).parts
            )
        ]
        return sorted(files)

    def resolve(self, target, current_file):
        """Ищет цель вики-ссылки; возвращает путь, якорь, причину отказа и кандидатов."""
        normalized_target = target.replace("\\", "/").strip()
        target_path, separator, fragment = normalized_target.partition("#")
        anchor = f"#{fragment}" if separator else ""
        if not target_path:
            return None, anchor, "empty target", set()

        explicit = target_path.lower()
        for key in (explicit, explicit + ".md"):
            if key in self.paths:
                matches = self.paths[key]
                if len(matches) == 1:
                    return next(iter(matches)), anchor, "", set()
                return None, anchor, "ambiguous path", matches

        name = explicit.rsplit("/", 1)[-1]
        matches = self.name_candidates(name)

        if not matches:
            return None, anchor, "target not found", set()
        if len(matches) == 1:
            return next(iter(matches)), anchor, "", set()
        same_directory = {path for path in matches if path.parent == current_file.parent}
        if len(same_directory) == 1:
            return next(iter(same_directory)), anchor, "", set()
        if same_directory:
            return None, anchor, "ambiguous in current directory", same_directory
        return None, anchor, "ambiguous target", matches

    def lookup_root(self, target):
        """Ищет путь от корня хранилища; возвращает файл и всех кандидатов."""
        key = target.lower()
        matches = set()
        for attempt in (key, key + ".md"):
            matches |= self.paths.get(attempt, set())
        if len(matches) == 1:
            return next(iter(matches)), matches
        return None, matches

    def name_candidates(self, target):
        """Возвращает файлы с таким именем без учёта каталога."""
        key = target.lower()
        matches = set(self.names.get(key, set()))
        if not matches and not key.endswith(".md"):
            matches = set(self.names.get(key + ".md", set()))
        return matches

    def is_note_relative(self, target, current_file):
        """Проверяет, что путь без префикса уже отсчитывается от заметки."""
        joined = posixpath.normpath(
            posixpath.join(current_file.parent.as_posix(), target)
        )
        if joined == ".." or joined.startswith("../"):
            return False
        return joined.lower() in self.files or (joined.lower() + ".md") in self.files

    def destination(self, resolved, current_file, anchor=""):
        """Строит относительный путь от заметки; пробелы требуют угловых скобок."""
        url = posixpath.relpath(resolved.as_posix(), current_file.parent.as_posix())
        if resolved.suffix.lower() == ".md" and url.endswith(".md"):
            url = url[:-3]
        url += anchor
        return f"<{url}>" if " " in url else url

    def convert_text(self, text, current_file):
        issues = []
        lines = []
        fence = None
        frontmatter = self.frontmatter_end(text)
        for number, line in enumerate(text.splitlines(keepends=True), 1):
            if frontmatter is not None and number <= frontmatter:
                lines.append(line)
                continue
            ending = "\n" if line.endswith("\n") else ""
            body = line[:-1] if ending else line
            match = FENCE.match(body)
            if fence:
                if match and match.group(1) == fence:
                    fence = None
                lines.append(line)
                continue
            if match:
                fence = match.group(1)
                lines.append(line)
                continue

            body = self.convert_wikilinks(body, current_file, number, issues)
            body = self.convert_markdown_links(body, current_file, number, issues)
            lines.append(body + ending)
        return "".join(lines), issues

    @staticmethod
    def frontmatter_end(text):
        """Возвращает номер последней строки frontmatter или None.

        Ссылки во frontmatter резолвит плагин `note-properties` по своим
        правилам, не учитывая `markdownLinkResolution`, поэтому YAML
        остаётся как написан.
        """
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return None
        for number, line in enumerate(lines[1:], 2):
            if line.strip() == "---":
                return number
        return None

    def convert_wikilinks(self, line, current_file, number, issues):
        def replace(match):
            is_embed = bool(match.group(1))
            parts = match.group(2).replace(r"\|", "|").split("|")
            target = parts[0].strip()
            alias = parts[1].strip() if len(parts) > 1 else ""

            if target == "blue_bible.pdf":
                return f"[{alias or 'синяя библия'}]({BLUE_BIBLE_URL})"

            resolved, anchor, reason, candidates = self.resolve(target, current_file)
            if resolved is None:
                issues.append((number, match.group(0), reason, candidates, "error"))
                return match.group(0)

            issues.append(
                (number, match.group(0), "wikilink can be converted", set(), "change")
            )
            url = self.destination(resolved, current_file, anchor)
            display = resolved.stem if resolved.suffix.lower() == ".md" else resolved.name
            if not is_embed:
                return f"[{alias or display}]({url})"
            alt = f"{display}|{alias}" if alias and WIDTH.match(alias) else (alias or display)
            return f"![{alt}]({url})"

        return sub_outside_code(WIKILINK, replace, line)

    def convert_markdown_links(self, line, current_file, number, issues):
        def replace(match):
            inner = match.group(3)
            new_inner = self.normalize_destination(
                inner, current_file, number, match.group(0), issues
            )
            if new_inner is None:
                return match.group(0)
            return f"{match.group(1)}[{match.group(2)}]({new_inner})"

        return sub_outside_code(MD_LINK, replace, line)

    def normalize_destination(self, inner, current_file, number, link, issues):
        raw = inner.strip()
        if not raw:
            return None
        dest = raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw
        if not dest or dest.startswith("#") or dest.startswith("//") or SCHEME.match(dest):
            return None

        target, separator, fragment = dest.partition("#")
        anchor = f"#{fragment}" if separator else ""
        if not target:
            return None
        target = target.replace("\\", "/")
        if target.startswith(("./", "../", "/")):
            # Paths written by the author relative to the note are left alone:
            # a link to a file that does not exist yet is legitimate.
            return None

        if self.is_note_relative(target, current_file):
            return None
        if "/" not in target:
            candidates = self.name_candidates(target)
            if not candidates:
                issues.append((number, link, "target not found", candidates, "error"))
            elif len(candidates) > 1:
                issues.append((number, link, "ambiguous target", candidates, "error"))
            else:
                issues.append(
                    (number, link, "target not found in the note directory", candidates, "error")
                )
            return None

        resolved, candidates = self.lookup_root(target)
        if resolved is None:
            reason = "ambiguous path" if candidates else "target not found"
            issues.append((number, link, reason, candidates, "error"))
            return None
        new = self.destination(resolved, current_file, anchor)
        if new == raw:
            return None
        issues.append((number, link, "can be made relative", set(), "change"))
        return new

    def run(self, check_only=False):
        updates = {}
        failures = 0

        for path in self.markdown_files():
            relative_path = path.relative_to(self.root_dir)
            text = path.read_text(encoding="utf-8")
            converted, issues = self.convert_text(text, relative_path)

            for number, link, reason, candidates, kind in issues:
                if kind == "error" or check_only:
                    message = f"{relative_path.as_posix()}:{number}: {reason}: {link}"
                    if candidates:
                        names = ", ".join(sorted(c.as_posix() for c in candidates))
                        message += f" (candidates: {names})"
                    print(message)
                    failures += 1

            if not check_only and converted != text:
                updates[path] = converted

        if failures:
            if check_only:
                print(f"Link check failed: {failures} link(s) need attention.")
            else:
                print(f"Link conversion aborted: {failures} unresolved link(s) found.")
                print("No files were modified.")
            return 1

        if check_only:
            print("Link check passed: no unconverted links")
            return 0

        for path, converted in updates.items():
            path.write_text(converted, encoding="utf-8", newline="\n")
        print(f"Link conversion passed: updated {len(updates)} file(s)")
        return 0


def main():
    modes = {"apply-all": False, "check": True, "--check": True}
    if len(sys.argv) != 2 or sys.argv[1] not in modes:
        print("Использование: python scripts/convert_links.py apply-all|check", file=sys.stderr)
        return 2

    converter = LinkConverter(CONTENT_ROOT)
    return converter.run(check_only=modes[sys.argv[1]])


if __name__ == "__main__":
    sys.exit(main())
