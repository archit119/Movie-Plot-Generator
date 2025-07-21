import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # 🔑 Loads from .env

MODEL = "gpt-4"
system_prompt = """
You are a Hollywood screenwriter who specializes in high-concept genre movies. 
You write punchy, dramatic stories that feel like blockbusters.
"""

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"), 
    model = MODEL, 
    temperature=0.8)

def call_llm(user_prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    return llm.invoke(messages).content  # ✅ only return the message content


