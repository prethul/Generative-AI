from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
import streamlit as st 
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage 


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

st.title("Amar-AI-ChatBot")
st.markdown("This is a Smart QNA-ChatBot")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message['role']
    content = message['content']
    st.chat_message('role').markdown(content)

user_input = st.chat_input("Ask me Anything.....")

if user_input:
    
    st.session_state.messages.append({'role' : 'user', 'content' : user_input})
    st.chat_message("user").markdown(user_input)
    result = llm.invoke(user_input)
    
    st.chat_message("ai").markdown(result.content)
    st.session_state.messages.append({'role' : 'ai', 'content' : result.content})
