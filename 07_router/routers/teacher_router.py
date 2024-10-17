from fastapi import APIRouter

teacher = APIRouter(
    prefix="/api/teachers",
    tags=["students"]
)

@teacher.get("/")
async def get_teacher():
    return{"message: 선생님입니다."}