from pathlib import Path
import re
import sys

site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
required = [
    site / "index.html",
    site / "repositories" / "index.html",
    site / "portfolio-status" / "index.html",
    site / "reports" / "index.html",
    site / "dashboard" / "index.html",
    # Compatibility endpoints for URLs published before clean routes were introduced.
    site / "repositories.md",
    site / "portfolio-status.md",
]
missing = [str(path) for path in required if not path.exists()]
if missing:
    raise SystemExit("Missing required published routes: " + ", ".join(missing))

index = (site / "index.html").read_text(encoding="utf-8", errors="replace")
if "just-the-docs" not in index.lower():
    raise SystemExit("Just the Docs theme asset was not detected in the generated homepage")

css_links = re.findall(r'href=["\']([^"\']+\.css[^"\']*)["\']', index)
if not css_links:
    raise SystemExit("No stylesheet was linked from the generated homepage")

errors = []
for html in site.rglob("*.html"):
    text = html.read_text(encoding="utf-8", errors="replace")
    for href in re.findall(r'href=["\']([^"\']+)["\']', text):
        # The two compatibility redirect pages are intentional. Other generated
        # navigation should never expose Markdown source URLs.
        if href.endswith(".md"):
            errors.append(f"{html}: source Markdown link exposed: {href}")
if errors:
    raise SystemExit("\n".join(errors))

for legacy, target in ((site / "repositories.md", "/repositories/"), (site / "portfolio-status.md", "/portfolio-status/")):
    text = legacy.read_text(encoding="utf-8", errors="replace")
    if target not in text:
        raise SystemExit(f"Legacy route {legacy} does not redirect to {target}")

print(f"Validated {len(list(site.rglob('*.html')))} HTML files, Just the Docs assets, clean routes, and legacy redirects.")
