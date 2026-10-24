from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
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

#first prompt 
prompt1 = template1.invoke({'topic_name' : 'RAG'})
result1 = llm.invoke(prompt1)
#second prompt
prompt2 = template2.invoke({'text' :result1.content})
result2 = llm.invoke(prompt2)

print(result2.content)