import urllib.request
import json
import re

def fetch_title(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
            return match.group(1).strip() if match else "No title found"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://github.com"
    ]
    
    results = {}
    for url in urls:
        print(f"Fetching title for {url}...")
        results[url] = fetch_title(url)
        
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
        
    print("Results saved to results.json")

if __name__ == "__main__":
    main()
