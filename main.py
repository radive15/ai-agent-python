from dotenv import load_dotenv
import os
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


@tool
def get_date() -> str:
    """Tampilkan tanggal hari ini."""
    return datetime.now().strftime("%Y-%m-%d")


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

system_prompt = """
Kamu adalah asisten AI bernama Luffy.
Jawab selalu dalam bahasa gaul indonesia.
Jika tidak tahu jawabannya, katakan tidak tahu.
"""

agent = create_react_agent(model=llm, tools=[get_date], prompt=system_prompt)

user_query = input("Masukan pertanyaan: ")

response = agent.invoke({"messages": [{"role": "user", "content": user_query}]})

print(response["messages"][-1].content)
