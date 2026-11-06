
from langchain_text_splitters import CharacterTextSplitter

text = '''
Artificial Intelligence (AI) is one of the most transformative technologies in the modern world. It enables machines and computer systems to perform tasks that normally require human intelligence, such as learning, problem-solving, decision-making, and understanding language. AI is widely used in healthcare, education, agriculture, transportation, banking, and business. In healthcare, AI helps doctors detect diseases and analyze medical reports more efficiently. In education, AI-powered tools provide personalized learning experiences and help students understand complex topics. Farmers can use AI to predict weather conditions, detect crop diseases, and improve agricultural production. Businesses use AI to automate repetitive tasks, analyze customer behavior, and make better decisions. AI also creates new career opportunities in fields such as machine learning, data science, robotics, and natural language processing. However, responsible use of AI is essential to protect privacy, reduce bias, and ensure security. Overall, AI has the potential to improve human life and create a smarter, more productive future.
'''

splitter = CharacterTextSplitter (
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_text(text)
print(result)
print("chunk number :",len(result))