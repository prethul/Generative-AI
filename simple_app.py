from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 


load_dotenv ()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite',
    temperature = 0.7
)

prompt = PromptTemplate(
    template = 'Suggest me a suitable movie name about this topic {topic}',
    input_variables = ['topic']
)

topic = input("Enter your topic : ")

formatted_topic = prompt.format(topic = topic)

result = llm.invoke(topic)
print("Suggested name :",result)