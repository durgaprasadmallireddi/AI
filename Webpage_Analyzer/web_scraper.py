import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetch HTML content from a given URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Remove script and style elements
    scope = soup(['script', 'style', 'header', 'footer', 'aside', 'nav', 'img', 'video','svg', 'source'])
    for element in scope:
        element.decompose()
    # Get text
    text = soup.get_text(separator=' ')
    # Clean up whitespace
    lines = (line.strip() for line in text.splitlines())
    text = ' '.join(line for line in lines if line)
    return text

def trim_text(text, max_length=10000):
    """Trim text to a maximum length."""
    if len(text) > max_length:
        return text[:max_length]
    return text

def scrape_website(url, max_length=10000):
    ''' Scrape text content from a website URL. '''
    try:
        html_content = fetch_html(url)
        if html_content:
            text = extract_text(html_content)
            trimmed_text = trim_text(text, max_length)
            return trimmed_text
        else:
            raise ValueError("No HTML content fetched")
    except ValueError:
        return "Error: Unable to retrieve content from the URL."
        