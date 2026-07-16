import unittest
import sys
import os

# add scripts dir to path so we can import fetch_titles
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from fetch_titles import fetch_title

class TestFetch(unittest.TestCase):
    def test_valid(self):
        t = fetch_title("https://example.com")
        self.assertIn("Example Domain", t)

    def test_bad_url(self):
        t = fetch_title("https://thiswebsitedoesnotexistatall.invalid")
        self.assertTrue(t.startswith("error:"))

if __name__ == '__main__':
    unittest.main()
