from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
1: {
"name": "john",
"age": 17,
"class": "year 12"
}
}

class Student (BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent (BaseModel):
    name: Optional [str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def home():
    return {"name":"it is testing"}



# the below is an example of the path parameter
@app.get("/get-student/{student_id}")
def get_student (student_id: int):
    return students[student_id]


# the below is an example for a query parameter
@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students [student_id]
    return {"Data": "Not found"}

@app.get("/get-by-name/{student_id}")
def get_students(student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students [student_id][ "name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students [student_id] = student
    return students[student_id]

@app.put(" /update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    student: UpdateStudent
    students [student_id] = student
    return students [student_id]