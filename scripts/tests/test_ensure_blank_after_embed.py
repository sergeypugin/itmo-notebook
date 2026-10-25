"""Тесты вставки пустой строки после вставок."""
import tempfile
import unittest
from pathlib import Path

from scripts.ensure_blank_after_embed import process_file, process_tree, rewrite


class EnsureBlankAfterEmbedTest(unittest.TestCase):
    def test_inserts_blank_before_text(self):
        self.assertEqual(rewrite("![x](a.png)\nтекст\n"), ("![x](a.png)\n\nтекст\n", True))

    def test_existing_blank_untouched(self):
        text = "![x](a.png)\n\nтекст\n"
        self.assertEqual(rewrite(text), (text, False))

    def test_embed_at_end_adds_nothing(self):
        for text in ("![x](a.png)", "![x](a.png)\n"):
            self.assertEqual(rewrite(text), (text, False))

    def test_blockquote_gets_quote_prefix(self):
        self.assertEqual(
            rewrite("> ![x](a.png)\n> текст\n"),
            ("> ![x](a.png)\n>\n> текст\n", True),
        )

    def test_blockquote_blank_already_valid(self):
        text = "> ![x](a.png)\n>\n> текст\n"
        self.assertEqual(rewrite(text), (text, False))

    def test_wikilink_embed(self):
        self.assertEqual(rewrite("![[x]]\nтекст\n"), ("![[x]]\n\nтекст\n", True))

    def test_two_embeds_in_a_row(self):
        self.assertEqual(
            rewrite("![a](a.png)\n![b](b.png)\nтекст\n"),
            ("![a](a.png)\n\n![b](b.png)\n\nтекст\n", True),
        )

    def test_fenced_block_untouched(self):
        text = "```\n![x](a.png)\nтекст\n```\n"
        self.assertEqual(rewrite(text), (text, False))

    def test_plain_link_untouched(self):
        for text in ("[x](a.png)\nтекст\n", "[[x]]\nтекст\n"):
            self.assertEqual(rewrite(text), (text, False))

    def test_embed_with_spaces_and_trailing_text(self):
        self.assertEqual(
            rewrite("![x](<a b.png>)\nтекст\n"),
            ("![x](<a b.png>)\n\nтекст\n", True),
        )

    def test_idempotent(self):
        once, _ = rewrite("![x](a.png)\nтекст\n")
        self.assertEqual(rewrite(once), (once, False))

    def test_process_tree_writes_only_changed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sub").mkdir()
            changed = root / "sub" / "a.md"
            stable = root / "b.md"
            changed.write_text("![x](a.png)\nтекст\n", encoding="utf-8", newline="\n")
            stable.write_text("![x](a.png)\n\nтекст\n", encoding="utf-8", newline="\n")

            result = process_tree(root)

            self.assertEqual(result, [Path("sub/a.md")])
            self.assertEqual(
                changed.read_text(encoding="utf-8"), "![x](a.png)\n\nтекст\n"
            )
            self.assertEqual(
                stable.read_text(encoding="utf-8"), "![x](a.png)\n\nтекст\n"
            )

    def test_frontmatter_skipped(self):
        self.assertEqual(
            rewrite("---\ntitle: x\n---\n![x](a.png)\nтекст\n"),
            ("---\ntitle: x\n---\n![x](a.png)\n\nтекст\n", True),
        )

    def test_unclosed_rule_is_not_frontmatter(self):
        self.assertEqual(
            rewrite("---\n\n![x](a.png)\nтекст\n"),
            ("---\n\n![x](a.png)\n\nтекст\n", True),
        )

    def test_process_file_returns_flag(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "a.md"
            path.write_text("![x](a.png)\n", encoding="utf-8", newline="\n")
            self.assertFalse(process_file(path))


if __name__ == "__main__":
    unittest.main()
