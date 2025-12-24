from openai import OpenAI
from web_scraper import scrape_website, extract_links, get_page_title
from dotenv import load_dotenv
import json
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

def get_relevant_links(url):
    """Get relevant links using AI from the webpage."""
    links = extract_links(url)
    system_prompt = """
    You are an expert web analyst. You are assigned a task to get relevant links from the list of links provided
    that could be used for generating a brochure about the main content of the webpage.
    identify and return only those that are most relevant to the main content of the webpage.
    Give me the links in the below JSON format:
    {
        {"linktype": "About Page", "url": "http://example.com/about"},
        {"linktype": "Services Page", "url": "http://example.com/services"},
        {"linktype": "Contact Page", "url": "http://example.com/contact"}
    }
    Only return the JSON object as output without any additional text."""
    user_prompt = """
    Here is the url of the webpage: {url}
    Here is the list of links:"""
    user_prompt += "\n".join(links)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    relevant_links = json.loads(response.choices[0].message.content)
    return relevant_links

def generate_brochure(url):
    relevant_links = get_relevant_links(url)
    system_prompt = """
    You are a skilled brochure designer. Using the relevant links provided,
    create a compelling and informative brochure that can be used for various marketing purposes.
    Structure the brochure with sections such as Introduction, Services, About Us, and Contact Information.
    Ensure the content is engaging and highlights the key aspects of the webpage.
    Just return the brochure content in Markdown format without any additional text."""
    user_prompt = "Here are the relevant links:\n"
    for link in relevant_links:
        user_prompt += f"{link['linktype']}: {link['url']}\n"
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    brochure_content = response.choices[0].message.content
    return brochure_content

if __name__ == "__main__":
    url = input("Enter the URL of the webpage to analyze or generate brochure: ")
    option = input("Choose an option - (1) Analyze Webpage, (2) Generate Brochure: ")
    if option == '1':
        print("Scraping the website...")
        text_content = scrape_website(url)

        if "Error" not in text_content:
            print("Analyzing text with Groq API...")
            analysis_result = analyze_text_with_groq(text_content, model)
            print("Analysis Result:")
            print(analysis_result)
        else:
            print("Error during scraping: Please check the URL and try again.")

    elif option == '2':
        brochure_content = generate_brochure(url)
        print("Generated Brochure Content.")
        page_title = get_page_title(url)
        filename = f"{page_title.replace(' ', '_')}_Brochure.md"
        # Save brochure to a markdown file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(brochure_content)
    else:
        print("Invalid option selected.")