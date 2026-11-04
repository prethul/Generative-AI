from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence, RunnableParallel , RunnablePassthrough , RunnableLambda 

load_dotenv ()

def word_coutner(text):
    return len (text.split())

runnable_word_coutner = RunnableLambda(word_coutner)

result = runnable_word_coutner.invoke("Hello this is Dipto howlader prethul. An AI engineer")
print(result)