from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
import streamlit as st 
from langchain_core.prompts import PromptTemplate 


load_dotenv ()

llm = ChatGroq(
    model = "openai/gpt-oss-20b",
    temperature = 0
)
st.header("Research Tool")



paper_input = st.selectbox("Select Research paper name",["Attention is all you need", "BERT Pretraining Deep learning model","Gpt-3 language models are few short learners"])

style_input = st.selectbox ("Select Explanation style" ,["Begineer-Friendlyt", "Medium", "Hard"])

length_input = st.selectbox ("Select length input",["2-3 lines paragraph","Medium 5-7 lines paragraph","Detailed explaination"])

template = PromptTemplate (
    
    template = """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
   - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.

""",
input_variables = ['paper_input', 'style_input','length_input']
    
)

prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
})

if st.button('Click me'):
    result = llm.invoke(prompt)
    st.write(result.content)
    
    