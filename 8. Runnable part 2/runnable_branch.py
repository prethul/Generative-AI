from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableBranch , RunnableLambda 
from dotenv import load_dotenv 

load_dotenv ()

frist_prompt = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ['topic']
)

second_prompt = PromptTemplate(
    template = 'Summarize the following text \n {text}',
    input_variables = ['text']
)

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

parser = StrOutputParser ()

report_chain = RunnableSequence(frist_prompt, llm, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500,RunnableSequence(second_prompt,llm,parser)),
    RunnablePassthrough ()
)

final_chain = RunnableSequence(report_chain , branch_chain)

result = final_chain.invoke({'topic' : 'Earthquake'})
print(result)