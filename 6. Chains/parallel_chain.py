from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm_1 = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

llm_2 = ChatGroq(
    model = 'openai/gpt-oss-120b'
)

prompt1 = PromptTemplate(
    template = 'Generate a summary on the following \n {text}',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 questions from the following text \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Merage the provided notes and quiz in a single document notes ->{notes} quiz -> {quiz}',
    input_variables = ['notes' , 'quiz']
)

parser = StrOutputParser ()

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | llm_1 | parser ,
        'quiz' : prompt2 |llm_2 | parser 
    }
)

marge_chain = prompt2 | llm_1 | parser 
final_chain = parallel_chain | marge_chain

text = """
Antonio, a Venetian merchant, complains to his friends of a melancholy that he cannot explain. His friend Bassanio is desperately in need of money to court Portia, a wealthy heiress who lives in the city of Belmont. Bassanio asks Antonio for a loan in order to travel in style to Portia’s estate. Antonio agrees, but is unable to make the loan himself because his own money is all invested in a number of trade ships that are still at sea. Antonio suggests that Bassanio secure the loan from one of the city’s moneylenders and name Antonio as the loan’s guarantor. In Belmont, Portia expresses sadness over the terms of her father’s will, which stipulates that she must marry the man who correctly chooses one of three caskets. None of Portia’s current suitors are to her liking, and she and her lady-in-waiting, Nerissa, fondly remember a visit paid some time before by Bassanio.

In Venice, Antonio and Bassanio approach Shylock, a Jewish moneylender, for a loan. Shylock nurses a long-standing grudge against Antonio, who has made a habit of berating Shylock and other Jews for their usury, the practice of loaning money at exorbitant rates of interest, and who undermines their business by offering interest-free loans. Although Antonio refuses to apologize for his behavior, Shylock acts agreeably and offers to lend Bassanio three thousand ducats with no interest. Shylock adds, however, that should the loan go unpaid, Shylock will be entitled to a pound of Antonio’s own flesh. Despite Bassanio’s warnings, Antonio agrees. In Shylock’s own household, his servant Launcelot decides to leave Shylock’s service to work for Bassanio, and Shylock’s daughter Jessica schemes to elope with Antonio’s friend Lorenzo. That night, the streets of Venice fill up with revelers, and Jessica escapes with Lorenzo by dressing as his page. After a night of celebration, Bassanio and his friend Gratiano leave for Belmont, where Bassanio intends to win Portia’s hand.

In Belmont, Portia welcomes the prince of Morocco, who has come in an attempt to choose the right casket to marry her. The prince studies the inscriptions on the three caskets and chooses the gold one, which proves to be an incorrect choice. In Venice, Shylock is furious to find that his daughter has run away, but rejoices in the fact that Antonio’s ships are rumored to have been wrecked and that he will soon be able to claim his debt. In Belmont, the prince of Arragon also visits Portia. He, too, studies the caskets carefully, but he picks the silver one, which is also incorrect. Bassanio arrives at Portia’s estate, and they declare their love for one another. Despite Portia’s request that he wait before choosing, Bassanio immediately picks the correct casket, which is made of lead. He and Portia rejoice, and Gratiano confesses that he has fallen in love with Nerissa. The couples decide on a double wedding. Portia gives Bassanio a ring as a token of love, and makes him swear that under no circumstances will he part with it. They are joined, unexpectedly, by Lorenzo and Jessica. The celebration, however, is cut short by the news that Antonio has indeed lost his ships, and that he has forfeited his bond to Shylock. Bassanio and Gratiano immediately travel to Venice to try and save Antonio’s life. After they leave, Portia tells Nerissa that they will go to Venice disguised as men.
"""


result = final_chain.invoke({'text':text}) 
print(result)
final_chain.get_graph().print_ascii()