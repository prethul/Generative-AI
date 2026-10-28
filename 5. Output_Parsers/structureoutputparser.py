from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_classic.output_parsers.structured import (
    StructuredOutputParser,
    ResponseSchema
)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

schema = [
    ResponseSchema(name ='fact_1' , description = 'Tell me about Fact_1'),
    ResponseSchema(name = 'fact_2' , description = 'Tell me about Fact_2'),
    ResponseSchema(name = 'fact_3' , description = 'Tell me about Fact_3')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about the {topics} \n {format_instruction}',
    input_variables = ['topics'],
    partial_variables = {'format_instruction' : parser.get_format_instructions()}
)

chain = template | llm | parser 

result = chain.invoke({'topics' : 'Generative-AI'})

print(result)