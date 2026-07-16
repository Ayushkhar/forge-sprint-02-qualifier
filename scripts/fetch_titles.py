import urllib.request
import json
import re
import os

def fetch_title(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='replace')
            match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
            if match:
                return re.sub(r'\s+', ' ', match.group(1)).strip()
            return "no title found"
    except Exception as e:
        return f"error: {e}"

def main():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://github.com"
    ]

    out = {}
    for url in urls:
        print(f"fetching {url}")
        out[url] = fetch_title(url)
        print(f"  -> {out[url]}")

    path = os.path.join(os.path.dirname(__file__), "results.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=4)
    print("saved to results.json")

if __name__ == "__main__":
    main()
