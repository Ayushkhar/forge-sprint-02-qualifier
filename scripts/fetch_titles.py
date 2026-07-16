"""
fetch_titles.py — Mini-Challenge submission for NMG Labs Forge Sprint 02.

Fetches the HTML <title> tag from a list of URLs and saves results to results.json.
Written by OpenClaw (coding agent) as instructed by Hermes (orchestrator agent).
"""

import urllib.request
import json
import re
import os


def fetch_title(url: str) -> str:
    """Fetch the HTML page title from a given URL.

    Args:
        url: The full URL to fetch (must include http/https).

    Returns:
        The page title as a string, or an error message if fetching fails.
    """
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Forge-Sprint-02-Bot/1.0)"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="replace")
            match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
            if match:
                # Clean up whitespace and HTML entities
                title = re.sub(r"\s+", " ", match.group(1)).strip()
                return title
            return "No title found"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Fetch titles for all target URLs and save results to results.json."""
    urls = [
        "https://example.com",
        "https://python.org",
        "https://github.com",
    ]

    results = {}
    for url in urls:
        print(f"Fetching: {url}")
        title = fetch_title(url)
        results[url] = title
        print(f"  -> {title}")

    # Save to results.json in the same directory as this script
    output_path = os.path.join(os.path.dirname(__file__), "results.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"\nResults saved to {output_path}")
    return results


if __name__ == "__main__":
    main()
