from fastapi import Depends, FastAPI
from requests import Session
from database import session_local, engine
import models, schemas, teacher_crud, student_crud

models.Base.metadata.create_all(bind= engine)

app = FastAPI()


# 제너레이터 함수
# 함수가 제너레이팅한 객체를 반환하게 하는 키워드
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
# teacher 등록
@app.post("/teachers", response_model=schemas.TeacherResponse)
async def create_teacher(
    teacher : schemas.TeacherCreate,
    db: Session = Depends(get_db)
):
    response = teacher_crud.create_teacher(db, teacher)
    
    return response

@app.get("/teacher/{teacher_id}", response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id: int, db: Session = Depends(get_db)):
    
    db_teacher = teacher_crud.get_teacher_by_id(db,teacher_id)
    
    return db_teacher

# teacher 전부 조회
@app.get("/teachers", response_model=list[schemas.TeacherResponse])
async def find_all_teachers(db: Session=Depends(get_db)):
    all_teachers = teacher_crud.get_all_teachers(db)
    return all_teachers

# teacher 수정
@app.put("/teachers/{teacher_id}",response_model=schemas.TeacherResponse)
async def update_teacher(
    teacher_id: int,
    teacher: schemas.TeacherUpdate,
    db: Session = Depends(get_db)
):
    update_teacher = teacher_crud.update_teahcer(db, teacher_id, teacher)
    
    return update_teacher


# 삭제
@app.delete("/teacher/{teacher_id}", status_code=204)
async def delete_teacher(teacher_id: int, db: Session= Depends(get_db)):
    teacher_crud.delete_teacher(db, teacher_id)
    return None




# studnet main==========================================================================

# student 등록
@app.post("/students", response_model=schemas.StudentResponse)
async def create_student(
    student : schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    response = student_crud.create_student(db, student)
    
    return response


@app.get("/student/{student_id}", response_model=schemas.StudentResponse)
async def find_student_by_id(student_id: int, db: Session = Depends(get_db)):
    
    db_student = student_crud.get_student_by_id(db,student_id)
    
    return db_student

# student 전부 조회
@app.get("/students", response_model=list[schemas.StudentResponse])
async def find_all_student(db: Session=Depends(get_db)):
    all_student = student_crud.get_all_student(db)
    return all_student

# student 수정
@app.put("/student/{student_id}",response_model=schemas.StudentResponse)
async def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    update_student = student_crud.update_teahcer(db, student_id, student)
    
    return update_student


# 삭제
@app.delete("/student/{student_id}", status_code=204)
async def delete_student(student_id: int, db: Session= Depends(get_db)):
    student_crud.delete_student(db, student_id)
    return None