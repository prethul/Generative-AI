from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence , RunnableLambda , RunnablePassthrough , RunnableParallel 


load_dotenv ()

def word_coutner(text):
    return len(text.split())

prompt = PromptTemplate(
    template = 'Write me a joke about {topic}',
    input_variables = ['topic']
)

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

parser = StrOutputParser ()

joke_chain = RunnableSequence(prompt,llm,parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_coutner)
})

final_chain = RunnableSequence(joke_chain,parallel_chain)

result = final_chain.invoke({'topic' : 'GenAI'})
print(result)