from langchain_groq import ChatGroq
from dotenv import load_dotenv 

load_dotenv ()

llm = ChatGroq(
    model = "openai/gpt-oss-20b",
    temperature = 0
)

result = llm.invoke("who is the current prime minister of bangladesh?")
print(result.content)