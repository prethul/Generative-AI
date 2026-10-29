from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel , RunnableLambda
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import BaseModel , Field 
from typing import Literal 
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite'
)

parser1 = StrOutputParser ()

class FeedBack(BaseModel):
    
    sentiment : Literal ['positive' , 'negative'] = Field(description = 'Give me the sentiment feedback')

parser2 = PydanticOutputParser (pydantic_object = FeedBack)
    

prompt1 = PromptTemplate(
    template = 'Classify the following text into postive and negtive feedback {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction':parser2.get_format_instructions()}
)

#positive feedback prompt
prompt2 = PromptTemplate(
    template = 'Write the approriate respone of this positive feedback \n {feedback}',
    input_variables = ['feedback']
)

#Negative feedback prompt
prompt3 = PromptTemplate(
    template = 'Write the approriate respone of this positive feedback \n {feedback}',
    input_variables = ['feedback']
)

classifier_chain = prompt1 | llm | parser2 

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | llm | parser1),
    (lambda x:x.sentiment == 'negative', prompt3 | llm | parser1),
    RunnableLambda (lambda x :'Could not find any sentiment')
)

chain = classifier_chain | branch_chain 

result = chain.invoke({'feedback':'This is a bad movie'})
print(result)