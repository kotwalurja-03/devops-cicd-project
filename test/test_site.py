
from pathlib import Path
import unittest

PROJECT_DIR = Path(__file__).resolve().parent.parent


class WebsiteTests(unittest.TestCase):

    def test_required_files_exist(self):
        required_files = [
            "index.html",
            "styles.css",
            "script.js",
        ]

        for filename in required_files:
            with self.subTest(filename=filename):
                self.assertTrue(
                    (PROJECT_DIR / filename).is_file(),
                    f"Missing required file: {filename}"
                )

    def test_html_has_required_elements(self):
        html = (PROJECT_DIR / "index.html").read_text(
            encoding="utf-8"
        )

        required_content = [
            'id="status"',
            'href="styles.css"',
            'src="script.js"',
            'id="overview"',
            'id="pipeline"',
            'id="tools"',
        ]

        for item in required_content:
            with self.subTest(item=item):
                self.assertIn(item, html)

    def test_javascript_updates_status(self):
        javascript = (PROJECT_DIR / "script.js").read_text(
            encoding="utf-8"
        )

        self.assertIn("Website loaded successfully", javascript)
        self.assertIn("getElementById", javascript)


if __name__ == "__main__":
    unittest.main()
