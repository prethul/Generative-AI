from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv 
from langchain_core.runnables import RunnableSequence,RunnableParallel


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a linkedln post about {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser ()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, llm, parser),
    'linkedln' : RunnableSequence(prompt2,llm,parser)
})

result = parallel_chain.invoke({'topic' : 'Cricket'})
print(result)