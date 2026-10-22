from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint

from dotenv import load_dotenv 

load_dotenv() 

llm = HuggingFaceEndpoint(
    model = "openai/gpt-oss-120b",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("Who is the current prime minister of Bangladesh?")
print(result)