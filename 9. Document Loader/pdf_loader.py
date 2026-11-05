from langchain_community.document_loaders import TextLoader,PyPDFLoader 
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv

load_dotenv()