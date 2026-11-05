from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv

load_dotenv ()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

prompt = PromptTemplate(
    template = 'Write a summary from the following {text}',
    input_variables = ['text']
)
 
parser = StrOutputParser()
 
loader = TextLoader('9. Document Loader/cricket.txt', encoding = 'utf-8') 

docs = loader.load()

chain = prompt | llm | parser 

result = chain.invoke({'text': docs[0].page_content})
print(result)

print(docs[0].metadata)