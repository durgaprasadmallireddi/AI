import json
from openai import OpenAI
import os
from dotenv import load_dotenv
import gradio as gr
from pathlib import Path
from tools import tool_schemas, tools

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
groq_base_url = os.getenv("GROQ_BASE_URL")
model = "openai/gpt-oss-120b"

def load_prompt(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

SYSTEM_PROMPT = load_prompt("prompts/system_prompt.md")

def chat(messages, history):
    client = OpenAI(api_key=groq_key, base_url=groq_base_url)
    history = [{'role': h['role'], 'content': h['content']} for h in history]
    messages = [{'role': 'system', 'content': SYSTEM_PROMPT}] + history + [{'role': 'user', 'content': messages}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tool_schemas.get_tools(),
    )
    print("Response:", response)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response = handle_tool_calls(message)
        messages.append(message)
        messages.append({'role': 'assistant', 'content': response})
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
    return response.choices[0].message.content

def handle_tool_calls(message):
    tool_calls = message.tool_calls
    for tool_call in tool_calls:
        if tool_call.function.name in tool_schemas.get_tool_names():
            params = json.loads(tool_call.function.arguments)
            response = tools.call_tool(tool_call.function.name, params)
            return json.dumps(response)
    return "Error: Unknown tool called."

if __name__ == "__main__":
    gr.ChatInterface(fn=chat, title="IRCTC Agent chatbot", 
                     description="An AI agent that helps you get information about trains, schedules, and availability.").launch()