import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from fetch_titles import fetch_title

class TestFetchTitles(unittest.TestCase):
    def test_fetch_valid_url(self):
        title = fetch_title("https://example.com")
        self.assertIn("Example Domain", title)

    def test_fetch_invalid_url(self):
        title = fetch_title("https://invalid.example.invalid")
        self.assertTrue(title.startswith("Error:"))

if __name__ == '__main__':
    unittest.main()
