import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = OpenAI(model='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
