from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from typing import TypedDict,Annotated,Optional,Literal  
from pydantic import BaseModel,Field 
load_dotenv()

model = ChatGoogleGenerativeAI(
    model ='gemini-2.5-flash'
)
#scehma 
class Review(BaseModel):
    
    
    key_themes : list[str] = Field(description = "Write down all the key themes")
    summary : str = Field (description = "A brief summary of the review")
    sentiment : Literal["pos","neg"] = Field (description = "Return the exact sentiment")
    words : int = Field (description ="Return the exact words of the summary")
    pros : Optional[list[str]] = Field (default = None,description = "Write down all the pros from the review")
    cons : Optional[list[str]] = Field (default = None,description ="Write down all the cons from the review")

    
structed_model = model.with_structured_output(Review)    
    
result = structed_model.invoke(""" iPhone 14 Review

The Apple iPhone 14 is a stylish and reliable smartphone that offers a premium design, excellent camera quality, and smooth performance. Its 6.1-inch Super Retina XDR OLED display delivers vibrant colors and sharp visuals, making it great for watching videos, browsing social media, and enjoying games. The glass back and aluminum frame give the phone an elegant look and a comfortable feel.

One of the best features of the iPhone 14 is its camera system. The 12MP main camera captures detailed photos with natural colors, while the ultra-wide camera is useful for landscapes and group pictures. It also offers impressive video recording capabilities, making it a good choice for photography lovers and content creators. Powered by the A15 Bionic chip, the phone handles everyday tasks, multitasking, and most games smoothly. Its iOS experience is user-friendly and works well with other Apple devices.

Although the iPhone 14 has a 60Hz display and does not offer the fastest charging speeds compared with some competitors, it still provides a satisfying overall experience. Battery performance is suitable for everyday use, depending on usage and battery condition. Overall, the iPhone 14 is a great option for anyone looking for a premium smartphone with dependable performance, an excellent camera, and an elegant design. Before purchasing, it is worth comparing its price with newer models to make sure you get the best value for your money.""")

print(result.key_themes)