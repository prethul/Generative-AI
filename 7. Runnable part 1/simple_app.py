from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
load_dotenv ()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash',
    temperature = 0.7
)

prompt = PromptTemplate(
    template = 'Suggest me a blog title {topic}',
    input_variables = ['topic']
)

topic = input("Enter a Topic :")

formatted_prompt = prompt.format(topic = topic)

blog_title = llm.invoke(formatted_prompt)

print("Generated blog title is :",blog_title)
