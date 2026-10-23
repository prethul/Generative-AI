from pydantic import BaseModel ,EmailStr, Field
from typing import TypedDict,Optional


class Student(BaseModel):
    
    name :  str ='prethul'
    age : Optional[int] = None 
    email : EmailStr
    cgpa : float = Field(gt=0,lt=5) 
    
new_student = {'age' : 22,'email' :'abc@gmail.com','cgpa' : 4}  

student = Student(**new_student)  
print(student)