# AI Webpage Analyzer

A simple Python project that takes a website URL, extracts readable content, and uses an LLM to generate a concise summary of the webpage.

This project is built as a **Hands-on exercise** while learning Large Language Models (LLMs).

---

## What this project does
- Accepts a public webpage URL
- Extracts text content from the webpage
- Removes non-text elements (scripts, images, videos, etc.)
- Groups content using webpage headings
- Sends the cleaned content to an LLM for summarization

---

## Tech Stack
- Python
- Requests
- BeautifulSoup
- OpenAI Python SDK (used with OpenAI-compatible APIs)
- LLaMA model via Groq

---

## How it works (high level)
1. Fetches HTML content from the given URL
2. Cleans and extracts readable text
3. Organizes text based on HTML headings
4. Sends the processed text to an LLM
5. Returns a short, human-readable summary

---

## Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
GROQ_API_KEY=your_groq_api_key

#Usage
python main.py
```
Provide a public webpage URL when prompted.

## Notes
- Designed for static public webpages (wikipedia)
- Does not support login-required or JS-heavy sites
- Implementation is intentionally kept simple


