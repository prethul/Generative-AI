
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    max_completion_tokens = 10
)

result = model.invoke("What is the capital of bangladesh")
print(result.content)