from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model ='gemini-2.5-flash'
)

#first prompt 
template1 = PromptTemplate(
    template = "Write a detailed explaination about {topic_name}",
    input_variables = ['topic_name']
)
#second prompt 
template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text {text}",
    input_variables = ['text']
)

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({'topic_name' : 'Generative-AI'})

print(result)