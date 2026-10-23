
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.title("Amar-AI ChatBot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


for chat in st.session_state['chat_history']:
    with st.chat_message(chat['role']):
        st.text(chat['content'])


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0
)
     
# chat input 
user_input = st.chat_input("Ask me Anything....")

if user_input:
    st.session_state['chat_history'].append({'role':'user', 'content' : user_input})
    with st.chat_message('user'):
        st.text(user_input)    
    
    
    response = model.invoke([
        HumanMessage(content=user_input)
    ])
    content = response.content

    if isinstance(content, list):
        ai_message = "\n".join(
        item["text"]
        for item in content
        if isinstance(item, dict) and item.get("type") == "text"
    )
    else:
        ai_message = content
        st.session_state['chat_history'].append({'role' :'assistant', 'content' :ai_message})
        with st.chat_message('assistant'):
            st.markdown(ai_message)       

