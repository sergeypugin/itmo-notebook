#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
CONTENT_ROOT = REPO_ROOT / "itmo-notebook"
BLUE_BIBLE_URL = "https://se.ifmo.ru/documents/10180/38002/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5+%D0%B2+%D0%9C%D0%B8%D0%BA%D1%80%D0%BE%D0%AD%D0%92%D0%9C/3e6ac9c1-5b92-4f49-ae32-1a00fb9b021c"
WIKILINK = re.compile(r"!?\[\[([^\]]*)\]\]", re.DOTALL)
IGNORED_DIRS = {".obsidian", "_ignore", ".git", "node_modules"}

# Media extensions that should remain as markdown images (not transcluded)
MEDIA_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg",
    ".mp4", ".webm", ".mov", ".avi", ".mkv",
    ".mp3", ".wav", ".ogg", ".flac",
    ".pdf",
}


class LinkConverter:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.paths = {}
        self.names = {}
        self.build_index()

    def build_index(self):
        for path in self.markdown_files():
            relative_path = path.relative_to(self.root_dir)
            self.add_index_entry(relative_path.as_posix(), relative_path)
            self.add_index_entry(relative_path.with_suffix("").as_posix(), relative_path)
            self.add_index_entry(path.name, relative_path)
            self.add_index_entry(path.stem, relative_path)

        for path in self.root_dir.rglob("*"):
            relative_parts = path.relative_to(self.root_dir).parts
            if path.is_file() and path.suffix.lower() != ".md" and not any(
                part in IGNORED_DIRS for part in relative_parts
            ):
                relative_path = path.relative_to(self.root_dir)
                self.add_index_entry(relative_path.as_posix(), relative_path)
                self.add_index_entry(path.name, relative_path)
                self.add_index_entry(path.stem, relative_path)

    def add_index_entry(self, key, path):
        normalized_key = key.lower().replace("\\", "/")
        paths = self.paths if "/" in normalized_key else self.names
        paths.setdefault(normalized_key, set()).add(path)

    def markdown_files(self):
        for path in self.root_dir.rglob("*.md"):
            relative_parts = path.relative_to(self.root_dir).parts
            if not any(part in IGNORED_DIRS for part in relative_parts):
                yield path

    def resolve_path(self, target, current_file):
        normalized_target = target.replace("\\", "/").strip()
        target_path, separator, fragment = normalized_target.partition("#")
        anchor = f"#{fragment}" if separator else ""
        if not target_path:
            return None, anchor, "empty target", set()

        explicit_path = target_path.lower()
        if explicit_path in self.paths:
            matches = self.paths[explicit_path]
            if len(matches) == 1:
                return next(iter(matches)), anchor, "", set()
            return None, anchor, "ambiguous path", matches

        if not explicit_path.endswith(".md") and f"{explicit_path}.md" in self.paths:
            matches = self.paths[f"{explicit_path}.md"]
            if len(matches) == 1:
                return next(iter(matches)), anchor, "", set()
            return None, anchor, "ambiguous path", matches

        name = target_path.rsplit("/", 1)[-1].lower()
        matches = set(self.names.get(name, set()))
        if not matches and not name.endswith(".md"):
            matches = set(self.names.get(f"{name}.md", set()))

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

    def _format_destination(self, url: str) -> str:
        """Wrap destination in angle brackets if it contains spaces."""
        return f"<{url}>" if " " in url else url

    def _is_media(self, path: Path) -> bool:
        return path.suffix.lower() in MEDIA_EXTS

    def convert_text(self, text, current_file):
        unresolved = []

        def replace_link(match):
            raw_content = match.group(1)
            parts = raw_content.replace(r"\|", "|").split("|")
            target = parts[0].strip()
            alias = parts[1].strip() if len(parts) > 1 else None

            if target == "blue_bible.pdf":
                return f"[{alias or 'синяя библия'}]({BLUE_BIBLE_URL})"

            resolved, anchor, reason, candidates = self.resolve_path(target, current_file)
            if resolved is None:
                line_number = text.count("\n", 0, match.start()) + 1
                unresolved.append((line_number, match.group(0), reason, candidates))
                return match.group(0)

            is_embed = match.group(0).startswith("!")
            url_path = resolved.as_posix()
            display_name = resolved.stem if resolved.suffix.lower() == ".md" else resolved.name

            # Determine if target is a note (.md) or media
            is_note = resolved.suffix.lower() == ".md"

            if is_note:
                url_path = url_path[:-3]  # strip .md
            url = quote(url_path, safe="/#") + anchor
            url = self._format_destination(url)

            if is_embed:
                # Embed: ![alt](path) - will be transcluded by transformer for notes,
                # rendered as image for media
                # If alias is a digit, treat as width hint (Obsidian syntax: |WIDTH)
                if alias and alias.isdigit():
                    return f"![{display_name}|{alias}]({url})"
                return f"![{alias or display_name}]({url})\n"
            return f"[{alias or display_name}]({url})"

        return WIKILINK.sub(replace_link, text), unresolved

    def run(self, check_only=False):
        unresolved_count = 0
        updates = {}

        for path in self.markdown_files():
            relative_path = path.relative_to(self.root_dir)
            content = path.read_text(encoding="utf-8")

            if check_only:
                for match in WIKILINK.finditer(content):
                    parts = match.group(1).replace(r"\|", "|").split("|")
                    target = parts[0].strip()
                    _, _, reason, candidates = self.resolve_path(target, relative_path)
                    reason = reason or "wikilink remains unconverted"
                    line_number = content.count("\n", 0, match.start()) + 1
                    msg = f"{path.relative_to(REPO_ROOT).as_posix()}:{line_number}: {reason}: {match.group(0)}"
                    if candidates:
                        cand_str = ", ".join(c.as_posix() for c in sorted(candidates))
                        msg += f" (candidates: {cand_str})"
                    print(msg)
                    unresolved_count += 1
                continue

            converted, unresolved = self.convert_text(content, relative_path)
            for line_number, link, reason, candidates in unresolved:
                msg = f"{path.relative_to(REPO_ROOT).as_posix()}:{line_number}: {reason}: {link}"
                if candidates:
                    cand_str = ", ".join(c.as_posix() for c in sorted(candidates))
                    msg += f" (candidates: {cand_str})"
                print(msg)
                unresolved_count += 1

            if converted != content:
                updates[path] = converted

        if unresolved_count > 0:
            if not check_only:
                print(f"\nLink conversion aborted: {unresolved_count} unresolved/ambiguous wikilink(s) found.")
                print("No files were modified. Please fix the links above and try again.")
            else:
                print(f"\nLink check failed: {unresolved_count} unconverted wikilink(s) found.")
            return 1

        if not check_only:
            for path, converted in updates.items():
                path.write_text(converted, encoding="utf-8", newline="\n")
            print(f"Link conversion passed: updated {len(updates)} file(s)")
        else:
            print("Link check passed: no wikilinks found")

        return 0


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"apply-all", "check"}:
        print("Usage: python scripts/convert_links.py apply-all|check")
        return 2

    converter = LinkConverter(CONTENT_ROOT)
    return converter.run(check_only=sys.argv[1] == "check")


if __name__ == "__main__":
    sys.exit(main())
