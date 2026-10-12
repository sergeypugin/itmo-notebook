#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
CONTENT_ROOT = REPO_ROOT / 'itmo-notebook'

BLUE_BIBLE_URL = "https://se.ifmo.ru/documents/10180/38002/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5+%D0%B2+%D0%9C%D0%B8%D0%BA%D1%80%D0%BE%D0%AD%D0%92%D0%9C/3e6ac9c1-5b92-4f49-ae32-1a00fb9b021c"

class LinkConverter:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.file_index = self._build_index()

    def _build_index(self):
        index = {}
        for root, _, files in os.walk(self.root_dir):
            for f in files:
                full_path = Path(root) / f
                rel_path = full_path.relative_to(self.root_dir)
                name = f
                stem = full_path.stem

                index.setdefault(name.lower(), []).append(rel_path)
                if name.lower() != stem.lower():
                    index.setdefault(stem.lower(), []).append(rel_path)
        return index

    def resolve_path(self, target, current_file_rel):
        target_clean = target.replace('\\', '/').strip()
        if not target_clean:
            return None, ""

        anchor = ""
        if '#' in target_clean:
            target_clean, anchor = target_clean.split('#', 1)
            anchor = '#' + anchor

        search_path = target_clean if target_clean.lower().endswith('.md') else target_clean + '.md'
        for paths in self.file_index.values():
            for p in paths:
                p_posix = p.as_posix().lower()
                if p_posix == target_clean.lower() or p_posix == search_path.lower():
                    return p, anchor

        name = target_clean.split('/')[-1].lower()
        matches = self.file_index.get(name, [])
        if not matches:
            matches = self.file_index.get(name + '.md', [])

        if not matches:
            return None, anchor

        if len(matches) == 1:
            return matches[0], anchor

        current_root = current_file_rel.parts[0] if current_file_rel.parts else None
        if current_root:
            same_section_matches = [p for p in matches if p.parts and p.parts[0] == current_root]
            if same_section_matches:
                same_dir_matches = [p for p in same_section_matches if p.parent == current_file_rel.parent]
                if same_dir_matches:
                    return same_dir_matches[0], anchor
                return same_section_matches[0], anchor

        return matches[0], anchor

    def convert_text(self, text, file_rel_path):
        pattern = re.compile(r'(!?)\[\[(.*?)\]\]')

        def replace_link(match):
            prefix = match.group(1)
            content = match.group(2)

            parts = content.replace(r'\|', '|').split('|')
            target_raw = parts[0].strip()
            alias = parts[1].strip() if len(parts) > 1 else None

            if target_raw == 'blue_bible.pdf':
                display = alias if alias else 'синяя библия'
                return f'[{display}]({BLUE_BIBLE_URL})'

            resolved, anchor = self.resolve_path(target_raw, file_rel_path)

            if resolved:
                if resolved.suffix == '.md':
                    url_path = resolved.as_posix()[:-3]
                else:
                    url_path = resolved.as_posix()
            else:
                print(f"Warning: Could not resolve '{target_raw}' in {file_rel_path}")
                url_path = target_raw.replace(' ', '%20')

            url_encoded = url_path.replace(' ', '%20')

            if prefix == '!':
                if alias and alias.isdigit():
                    return f'![{resolved.name if resolved else target_raw}|{alias}]({url_encoded}{anchor})'

                alt_text = alias if alias else (resolved.stem if resolved and resolved.suffix == '.md' else (resolved.name if resolved else target_raw))
                return f'![{alt_text}]({url_encoded}{anchor})'

            default_display = (resolved.name if resolved.suffix != '.md' else resolved.stem) if resolved else target_raw
            display_text = alias if alias else default_display
            return f'[{display_text}]({url_encoded}{anchor})'

        return pattern.sub(replace_link, text)

    def convert_file(self, file_rel_path):
        path = self.root_dir / file_rel_path
        if not path.exists():
            return False

        try:
            content = path.read_text(encoding='utf-8')
            new_content = self.convert_text(content, file_rel_path)
            if content != new_content:
                path.write_text(new_content, encoding='utf-8')
                return True
        except Exception as e:
            print(f"Error processing {file_rel_path}: {e}")
        return False

    def process_all(self):
        changed_total = 0
        for root, _, files in os.walk(self.root_dir):
            if any(x in root for x in ['.obsidian', '.git', 'node_modules', '_ignore']):
                continue
            for f in files:
                if f.endswith('.md'):
                    path = Path(root) / f
                    rel_path = path.relative_to(self.root_dir)
                    if self.convert_file(rel_path):
                        print(f"Converted: {rel_path}")
                        changed_total += 1
        print(f"\nTotal files updated: {changed_total}")

if __name__ == "__main__":
    converter = LinkConverter(CONTENT_ROOT)

    if len(sys.argv) > 1 and sys.argv[1] == 'apply-all':
        converter.process_all()
    else:
        print("Usage: python scripts/convert_links.py apply-all")
