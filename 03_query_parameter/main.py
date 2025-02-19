from fastapi import FastAPI

app = FastAPI()

# 쿼리 파라미터
# url 뒤에 ? 키-벨류 쌍으로 들어가는 파라미터

@app.get("/teachers/")
async def print_teacher_num(num: int, name: str):
    return {f"num: {num}, name: {name}"}

# 쿼리 매개변수를 필수로 만들려면 기본값을 설정안하면 된다.
# 다양한 매개변수를 작성할 때, 매개변수는 이름을 ㅗ 찾아지기 때문에 순서는 상관 x


# 선택적 매개변수
from typing import Union

@app.get("/teacher/{teacher_id}")
async def print_teacher(
    teacher_id: int, # path parameter
    name : str # query parameter
):
    return {f"teacher_id: {teacher_id}, teacher_name: {name}"}






