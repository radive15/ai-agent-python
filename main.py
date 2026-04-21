from dotenv import load_dotenv
import os
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_date():
    """ tampilkan tanggal hari ini """
    return datetime.now().strftime("%y-%m-%d")


llm = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview")

system_prompt = """
Anda sangat membantu 
"""


agent = create_agent(model=llm, tools=[get_date], system_prompt=system_prompt)
user_query = input("Masukan pertanyaan: ")

agent.invoke = ({"message":[{"role": "user", "content": user_query}]})