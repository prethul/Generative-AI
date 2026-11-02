from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv 

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a jokes about the {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser ()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

prompt2 = PromptTemplate(
    template = 'Generate the explaination of this {jokes}',
    input_variables =['jokes']
)

joke_chain = RunnableSequence(prompt1,llm,parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough (),
    'explaination' : RunnableSequence(prompt2,llm,parser)
})

final_chain = RunnableSequence (joke_chain, parallel_chain)
result = final_chain.invoke({'topic' : 'Cricket'})
print(result)