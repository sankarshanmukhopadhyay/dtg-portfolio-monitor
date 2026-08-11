from pathlib import Path
from urllib.parse import urlparse
import re
import sys

site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
required = [
    site / "index.html",
    site / "repositories" / "index.html",
    site / "portfolio-status" / "index.html",
    site / "reports" / "index.html",
    site / "dashboard" / "index.html",
    site / "domain-brief" / "index.html",
    site / "domain-model" / "index.html",
    site / "repositories.md",
    site / "portfolio-status.md",
]
missing = [str(path) for path in required if not path.exists()]
if missing:
    raise SystemExit("Missing required published routes: " + ", ".join(missing))

index = (site / "index.html").read_text(encoding="utf-8", errors="replace")

# Validate the rendered Just the Docs structure rather than depending on a
# particular asset filename or exact class-attribute ordering. Theme releases
# may add extra class tokens while retaining the same layout contract.
class_attributes = re.findall(r'class=["\']([^"\']+)["\']', index)
class_tokens = {
    token
    for attribute in class_attributes
    for token in attribute.split()
}
required_layout_classes = {"side-bar", "site-header", "main"}
missing_classes = sorted(required_layout_classes - class_tokens)
if missing_classes:
    raise SystemExit(
        "Generated homepage does not contain the expected Just the Docs layout classes: "
        + ", ".join(missing_classes)
        + ". Ensure normal pages receive layout: default."
    )

css_links = re.findall(r'href=["\']([^"\']+\.css(?:\?[^"\']*)?)["\']', index)
if not css_links:
    raise SystemExit("No stylesheet was linked from the generated homepage")

# At least one linked local stylesheet must exist in the built site. Strip the
# project Pages base path before resolving it against _site.
local_css = []
for href in css_links:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        continue
    path = parsed.path
    marker = "/dtg-portfolio-monitor/"
    if marker in path:
        path = path.split(marker, 1)[1]
    else:
        path = path.lstrip("/")
    candidate = site / path
    if candidate.exists():
        local_css.append(candidate)
if not local_css:
    raise SystemExit(
        "None of the local stylesheets linked from the homepage exist in the generated site"
    )

errors = []
for html in site.rglob("*.html"):
    text = html.read_text(encoding="utf-8", errors="replace")
    for href in re.findall(r'href=["\']([^"\']+)["\']', text):
        if href.endswith(".md"):
            errors.append(f"{html}: source Markdown link exposed: {href}")
if errors:
    raise SystemExit("\n".join(errors))

for legacy, target in (
    (site / "repositories.md", "/repositories/"),
    (site / "portfolio-status.md", "/portfolio-status/"),
):
    text = legacy.read_text(encoding="utf-8", errors="replace")
    if target not in text:
        raise SystemExit(f"Legacy route {legacy} does not redirect to {target}")

print(
    f"Validated {len(list(site.rglob('*.html')))} HTML files, "
    f"Just the Docs layout, {len(local_css)} local stylesheet(s), clean routes, "
    "and legacy redirects."
)
