from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser 

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)
parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me a reason in this AI era how can i survive as Software Engineer or AI engineer \n {format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction' : parser.get_format_instructions() }
)

#prompt = template.format()
#result = llm.invoke(prompt)
#final_result = parser.parse(result.content)

chain =  template | llm | parser 

result = chain.invoke({})

print(result)
print(type(result))