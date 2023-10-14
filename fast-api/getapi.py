from fastapi import FastAPI 
app = FastAPI()

@app.get("/")
def index():
    return {"name":"First Data"}

students = {
    1:{
        "name":"John"
    }
}
@app.get("/get-student")
def get_student(student_id:int):
    return students[student_id]