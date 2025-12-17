from openai import OpenAI
from web_scraper import scrape_website
from dotenv import load_dotenv
import os

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
groq_base_url = os.getenv("GROQ_BASE_URL")
model = "meta-llama/llama-4-scout-17b-16e-instruct"

# Initialize OpenAI client with Groq API settings
client = OpenAI(api_key=groq_key, base_url=groq_base_url)

def analyze_text_with_groq(text, model):
    response = client.responses.create(
        model=model,
        instructions="Analyze the following text and provide a concise summary.",
        input=text
    )
    return response.output_text

if __name__ == "__main__":
    url = input("Enter the URL of the webpage to analyze: ")
    print("Scraping the website...")
    text_content = scrape_website(url)

    if "Error" not in text_content:
        print("Analyzing text with Groq API...")
        analysis_result = analyze_text_with_groq(text_content, model)
        print("Analysis Result:")
        print(analysis_result)
    else:
        print("Error during scraping: Please check the URL and try again.")