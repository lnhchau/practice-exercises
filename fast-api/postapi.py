from fastapi import FastAPI 
from pydantic import BaseModel
app = FastAPI()

students= {}

class Student(BaseModel):
    name:str 
    age:int 
@app.put("/create-student")
def create_student(student_id:int, student:Student):
    students[student_id] = student
    return students