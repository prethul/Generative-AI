from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate the detailed report about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 pointers from the following text \n {text}',
    input_variables = ['text']
    
)

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

parser = StrOutputParser () 

chain = prompt1 | llm | parser | prompt2 | llm | parser 

result = chain.invoke({'topic':'Cricket'})
print(result)