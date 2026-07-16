import json
import urllib.request
import urllib.error
from html.parser import HTMLParser

class FirstTitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title_parts = []
        self.in_title = False
        self.done = False

    def handle_starttag(self, tag, attrs):
        if self.done:
            return
        if tag.lower() == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if self.done:
            return
        if tag.lower() == 'title':
            self.in_title = False
            self.done = True  # Stop capturing after the first <title> tag is closed

    def handle_data(self, data):
        if self.in_title and not self.done:
            self.title_parts.append(data)

    @property
    def title(self):
        return "".join(self.title_parts).strip() if self.title_parts else None

def get_title(url):
    print(f"Fetching: {url}")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read()
            encoding = response.headers.get_content_charset() or 'utf-8'
            try:
                html_str = html.decode(encoding, errors='replace')
            except Exception:
                html_str = html.decode('utf-8', errors='replace')
                
            parser = FirstTitleParser()
            parser.feed(html_str)
            title = parser.title
            return title if title else "No title found"
    except urllib.error.HTTPError as e:
        return f"HTTP Error {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://github.com"
    ]
    
    results = {}
    for url in urls:
        title = get_title(url)
        results[url] = title
        print(f"Result: {title}\n")
        
    output_file = "results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
        
    print(f"Saved results to {output_file}")

if __name__ == "__main__":
    main()
