from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence


load_dotenv()

prompt = PromptTemplate(
    template = 'Write a jokes about the {topic}',
    input_variables = ['topic']
)

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Explain every jokes {jokes}',
    input_variables =['jokes']
)

chain = RunnableSequence(prompt , llm , parser , prompt1 , llm , parser)

result = chain.invoke({'topic' : 'Gen-AI'})

print(result)