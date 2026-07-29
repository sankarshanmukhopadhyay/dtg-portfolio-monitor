import unittest
from dtg_monitor.intelligence import consolidate, normalise_title, theme_counts

class IntelligenceTests(unittest.TestCase):
    def test_normalises_conventional_commit_and_pr_suffix(self):
        self.assertEqual('add credential exchange', normalise_title('feat(vtc): add credential exchange (#42)'))
    def test_consolidates_commit_and_pull_request(self):
        base={'repository':'example/repo','title':'feat: same change','updated_at':'2026-01-01T00:00:00Z','url':'u','item_id':'1'}
        events=[{**base,'event_type':'commit'},{**base,'event_type':'pull_request','item_id':'2'}]
        result, collapsed=consolidate(events)
        self.assertEqual(1,len(result)); self.assertEqual(1,collapsed)
        self.assertEqual('pull_request',result[0]['event_type'])
    def test_theme_counts(self):
        counts=dict(theme_counts([{'title':'Credential revocation protocol','body':''}]))
        self.assertGreaterEqual(counts['credentials-and-proof'],1)
        self.assertGreaterEqual(counts['governance-and-lifecycle'],1)

if __name__=='__main__': unittest.main()
