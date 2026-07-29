from pathlib import Path
import re, sys
site=Path(sys.argv[1] if len(sys.argv)>1 else '_site')
required=[site/'index.html', site/'repositories/index.html', site/'portfolio-status/index.html', site/'reports/index.html']
missing=[str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing required published routes: '+', '.join(missing))
errors=[]
for html in site.rglob('*.html'):
    text=html.read_text(encoding='utf-8', errors='replace')
    for href in re.findall(r'href=["\']([^"\']+)["\']', text):
        if href.endswith('.md'):
            errors.append(f'{html}: source Markdown link exposed: {href}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated {len(list(site.rglob("*.html")))} HTML files and required routes.')
