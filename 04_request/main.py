from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/items/")
async def read_items(request : Request):
    # 클라이언트 ip
    host = request.client.host
    # Request 객체로 확인 가능한 것
    # body(): 본문
    #headers: 헤더
    return {"clienthost": host}


# request Body
# 클래스타입으로 만들고, BaseModel을 상속받아 구현한다.
from pydantic import BaseModel

class Teacher(BaseModel):
    is_working : bool
    name: str
    nickname: str | None = None # optional
    
@app.post("/teachers")
async def techer_info (teacher: Teacher):
    
    if teacher.nickname:
        return f"안녕하세요 제 닉네임은 {teacher.nickname}이고, 현재 일하는 상태는 {teacher.is_working} 이다. "
    return f"안녕하세요 제 이름은 {teacher.name}이고, 현재 일하는 상태는 {teacher.is_working} 이다."


# FastAPI
# path_parameter -> url에 선언을 한다.
# query-parameter -> 클래스 타입의 매개변수라면
# requestBody -> 그외

# student_no : path_parameter로 받고 int
# Student : requestBody( 이름 (str), 나이(int))
# (str)lecture_name : query_prarmeter

# student no, name, age, lecture_name을 전부 출력하는
# 문자열로 returen해주는 api


class Student(BaseModel):
    name: str
    age : int
    
@app.post("/students/{student_no}")
async def student_info (student: Student, student_no:int, lecture_name:str):
    return f"안녕하세요 저는 {student_no}를 가진 학생입니다. 이름은 {student.name}이고, 나이는 {student.age}살, {lecture_name}을 듣고 있습니다. "
