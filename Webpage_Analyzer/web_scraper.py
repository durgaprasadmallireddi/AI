import requests
from bs4 import BeautifulSoup

# Global headers for HTTP requests
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }

def fetch_html(url):
    """Fetch HTML content from a given URL."""
    try:
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
        
def extract_links(url):
    """Extract all hyperlinks from a given URL."""
    html_content = fetch_html(url)
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        if a_tag['href'].startswith('http') or a_tag['href'].startswith('https'):
            links.append(a_tag['href'])
    return links

def get_page_title(url):
    """Extract the title of the webpage."""
    html_content = fetch_html(url)
    if not html_content:
        return "No Title Found"
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.string.strip()
    return "No Title Found"