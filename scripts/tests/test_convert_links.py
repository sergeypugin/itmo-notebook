"""Тесты преобразования ссылок в относительные."""
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from scripts.convert_links import LinkConverter


class ConvertLinksTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")

    def read(self, relative):
        return (self.root / relative).read_bytes().decode("utf-8")

    def convert(self, mode="apply-all"):
        output = io.StringIO()
        with redirect_stdout(output):
            code = LinkConverter(self.root).run(check_only=mode == "check")
        return code, output.getvalue()

    def test_embed_with_width(self):
        self.write("matan/sem2/Attachments/pic.png", "x")
        self.write("matan/sem2/note.md", "![[pic.png|200]]\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("matan/sem2/note.md"), "![pic.png|200](Attachments/pic.png)\n")

    def test_embed_with_all_size_forms(self):
        self.write("matan/sem2/Attachments/pic.png", "x")
        self.write(
            "matan/sem2/note.md",
            "![[pic.png|200]] ![[pic.png|200x200]] ![[pic.png|x150]]\n",
        )

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(
            self.read("matan/sem2/note.md"),
            "![pic.png|200](Attachments/pic.png)"
            " ![pic.png|200x200](Attachments/pic.png)"
            " ![pic.png|x150](Attachments/pic.png)\n",
        )

    def test_wikilink_alias_drops_extension(self):
        self.write("matan/sem2/note.md", "x\n")
        self.write("matan/sem2/x.md", "[[note|текст]]\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("matan/sem2/x.md"), "[текст](note)\n")

    def test_wikilink_anchor_kept_verbatim(self):
        self.write("matan/sem2/note.md", "# Заголовок\n\nблок\n")
        self.write("matan/sem2/x.md", "[[note#Заголовок]] [[note#^block]]\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(
            self.read("matan/sem2/x.md"),
            "[note](note#Заголовок) [note](note#^block)\n",
        )

    def test_root_markdown_path_becomes_relative(self):
        self.write("matan/sem2/note.md", "x\n")
        self.write("OPD/questions/q1.md", "x\n")
        self.write("matan/sem2/a.md", "[n](matan/sem2/note) [q](OPD/questions/q1)\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(
            self.read("matan/sem2/a.md"),
            "[n](note) [q](../../OPD/questions/q1)\n",
        )

    def test_already_relative_untouched(self):
        self.write("matan/sem2/question-9.md", "x\n")
        self.write("matan/sem2/a.md", "[s](question-9) [u](./question-9) [v](../sem2/question-9)\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(
            self.read("matan/sem2/a.md"),
            "[s](question-9) [u](./question-9) [v](../sem2/question-9)\n",
        )

    def test_dot_paths_to_missing_files_untouched(self):
        self.write("a.md", "[b](./missing) [c](../missing) [d](../../missing)\n")
        before = self.read("a.md")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("a.md"), before)

    def test_spaces_get_angle_brackets(self):
        self.write("OPD/questions/Attachments/my pic.png", "x")
        self.write("OPD/questions/a.md", "![p](<OPD/questions/Attachments/my pic.png>)\n")
        self.write("OPD/questions/b.md", "![[my pic.png]]\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("OPD/questions/a.md"), "![p](<Attachments/my pic.png>)\n")
        self.assertEqual(self.read("OPD/questions/b.md"), "![my pic.png](<Attachments/my pic.png>)\n")

    def test_width_in_destination_is_broken(self):
        self.write("a.md", "![имя](файл.png|200)\n")
        before = self.read("a.md")

        code, output = self.convert()

        self.assertEqual(code, 1)
        self.assertIn("target not found", output)
        self.assertEqual(self.read("a.md"), before)

    def test_width_suffix_is_part_of_the_path(self):
        self.write("Attachments/pic.png", "x")
        self.write("a.md", "![имя|200](Attachments/pic.png|200)\n")

        code, output = self.convert()

        self.assertEqual(code, 1)
        self.assertIn("Attachments/pic.png|200", output)

    def test_malformed_width_treated_as_alias(self):
        self.write("Attachments/pic.png", "x")
        self.write("a.md", "![[pic.png|200x]]\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("a.md"), "![200x](Attachments/pic.png)\n")

    def test_external_and_anchor_links_untouched(self):
        line = "[a](https://x.y) [b](mailto:a@b) [c](//cdn/x) [d](#Раздел) [e](tel:+1)\n"
        self.write("a.md", line)

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("a.md"), line)

    def test_code_is_untouched(self):
        text = (
            "```\n"
            "![[pic.png]]\n"
            "[x](missing/doc)\n"
            "```\n"
            "\n"
            "~~~\n"
            "[[note]]\n"
            "~~~\n"
            "\n"
            "`![[pic.png]]` и `[x](missing/doc)`\n"
        )
        self.write("a.md", text)

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("a.md"), text)

    def test_second_run_changes_nothing(self):
        self.write("matan/sem2/Attachments/pic.png", "x")
        self.write("OPD/questions/q1.md", "x\n")
        self.write("matan/sem2/a.md", "![[pic.png|200]] [q](OPD/questions/q1)\n")

        self.convert()
        first = self.read("matan/sem2/a.md")
        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("matan/sem2/a.md"), first)

    def test_all_broken_links_reported_and_nothing_written(self):
        names = ("a.md", "b.md", "c.md")
        for name in names:
            self.write(name, f"![x](missing-{name[:-3]}.png)\n")
        before = {name: self.read(name) for name in names}

        code, output = self.convert()

        self.assertEqual(code, 1)
        self.assertEqual(output.count("target not found"), 3)
        for name in names:
            self.assertIn(f"{name}:1", output)
            self.assertEqual(self.read(name), before[name])

    def test_ambiguous_name_from_other_directory(self):
        self.write("a/dup.md", "x\n")
        self.write("b/dup.md", "x\n")
        self.write("c/note.md", "[x](dup)\n")
        before = self.read("c/note.md")

        code, output = self.convert()

        self.assertEqual(code, 1)
        self.assertIn("ambiguous", output)
        self.assertEqual(self.read("c/note.md"), before)

    def test_check_reports_root_path_and_changes_nothing(self):
        self.write("a/n.md", "x\n")
        self.write("b/m.md", "[n](a/n)\n")

        code, output = self.convert("check")

        self.assertEqual(code, 1)
        self.assertIn("can be made relative", output)
        self.assertIn("b/m.md:1", output)
        self.assertEqual(self.read("b/m.md"), "[n](a/n)\n")

    def test_check_reports_broken_target(self):
        self.write("a.md", "[x](missing/doc)\n")

        code, output = self.convert("check")

        self.assertEqual(code, 1)
        self.assertIn("a.md:1: target not found", output)

    def test_self_link_becomes_dotless_name(self):
        self.write("matan/sem3/index.md", "x\n")
        self.write("matan/sem3/a.md", "[i](matan/sem3/index)\n")

        code, output = self.convert()

        self.assertEqual(code, 0, output)
        self.assertEqual(self.read("matan/sem3/a.md"), "[i](index)\n")


if __name__ == "__main__":
    unittest.main()
