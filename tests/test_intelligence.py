import unittest
from dtg_monitor.intelligence import consolidate, normalise_title, theme_counts


class IntelligenceTests(unittest.TestCase):
    def test_normalises_conventional_commit_and_pr_suffix(self):
        self.assertEqual('add credential exchange', normalise_title('feat(vtc): add credential exchange (#42)'))

    def test_consolidates_commit_and_pull_request(self):
        base = {
            'repository': 'example/repo',
            'title': 'feat: same change',
            'updated_at': '2026-01-01T00:00:00Z',
            'url': 'u',
            'item_id': '1',
            'significance': 'high',
            'significance_score': 60,
            'significance_reasons': ['interoperability'],
            'linked_repositories': ['example/other'],
        }
        events = [
            {**base, 'event_type': 'commit', 'event_id': 'commit-1'},
            {**base, 'event_type': 'pull_request', 'item_id': '2', 'event_id': 'pr-2'},
        ]
        result, collapsed = consolidate(events)
        self.assertEqual(1, len(result))
        self.assertEqual(1, collapsed)
        self.assertEqual('pull_request', result[0]['event_type'])
        self.assertEqual(2, result[0]['change_unit_size'])
        self.assertTrue(result[0]['change_unit_key'])
        self.assertEqual(['example/other'], result[0]['linked_repositories'])
        self.assertEqual(1, len(result[0]['correlated_events']))

    def test_consolidation_preserves_strongest_significance(self):
        common = {
            'repository': 'example/repo',
            'title': 'fix: authority contract',
            'updated_at': '2026-01-01T00:00:00Z',
            'url': 'u',
            'linked_repositories': [],
        }
        result, _ = consolidate([
            {**common, 'event_type': 'commit', 'item_id': 'a', 'significance': 'critical', 'significance_score': 90, 'significance_reasons': ['authority-semantics']},
            {**common, 'event_type': 'pull_request', 'item_id': '2', 'significance': 'medium', 'significance_score': 30, 'significance_reasons': ['interoperability']},
        ])
        self.assertEqual('critical', result[0]['significance'])
        self.assertEqual(90, result[0]['significance_score'])
        self.assertEqual(['authority-semantics', 'interoperability'], result[0]['significance_reasons'])

    def test_theme_counts(self):
        counts = dict(theme_counts([{'title': 'Credential revocation protocol', 'body': ''}]))
        self.assertGreaterEqual(counts['credentials-and-proof'], 1)
        self.assertGreaterEqual(counts['governance-and-lifecycle'], 1)


if __name__ == '__main__':
    unittest.main()
