
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

required_files = [
    ROOT / "index.html",
    ROOT / "styles.css",
    ROOT / "script.js",
]

errors = []

for file_path in required_files:
    if not file_path.is_file():
        errors.append(f"Missing required file: {file_path.name}")

if not errors:
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    required_content = [
        "<!DOCTYPE html>",
        "<html",
        "<title>",
        'id="status"',
        'href="styles.css"',
        'src="script.js"',
    ]

    for item in required_content:
        if item not in html:
            errors.append(f"HTML is missing required content: {item}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDATION PASSED")
print("Required files and HTML checks are present.")
