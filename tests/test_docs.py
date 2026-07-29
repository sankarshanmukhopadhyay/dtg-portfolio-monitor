import unittest
from pathlib import Path

class DocumentationTests(unittest.TestCase):
    def test_no_public_markdown_links(self):
        root=Path(__file__).resolve().parents[1]/'docs'
        bad=[]
        for path in root.glob('*.md'):
            for line in path.read_text(encoding='utf-8').splitlines():
                if '](' in line and '.md)' in line:
                    bad.append(f'{path.name}: {line}')
        self.assertEqual([],bad)
    def test_stable_permalink_frontmatter(self):
        root=Path(__file__).resolve().parents[1]/'docs'
        for name in ('repositories.md','portfolio-status.md','reports.md'):
            self.assertIn('permalink:',(root/name).read_text())

if __name__=='__main__': unittest.main()
