from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader 

loader = PyPDFLoader('10. Text splitters\AI_Revolution_in_Bangladesh_English.pdf')

docs = loader.load()

splitter = CharacterTextSplitter (
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)
print(result)
print("chunk number :",len(result))
print(result[0].metadata)