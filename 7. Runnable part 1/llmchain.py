from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_classic.chains import LLMChain 

load_dotenv ()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

prompt = PromptTemplate(
    template = 'suggest me a some books name about these topics {topic}',
    input_variables = ['topic']
)

chain = LLMChain(llm=llm, prompt=prompt)

topic = input("Enter a topic :")

output = chain.run(topic)
print(output)



