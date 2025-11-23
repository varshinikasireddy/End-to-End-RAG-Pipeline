import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load your API key
load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Test it!
response = llm.invoke("Hello! Can you hear me?")
print("LLM Response:", response.content)