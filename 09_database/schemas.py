from pydantic import BaseModel
from typing_extensions import Optional

# request 받거나, response를 받을 때
# 기본 형식을 만들어 놓을 수 있다.
class TeacherBase(BaseModel):
    name: str
    is_active: bool
    nickname: Optional[str] = None
    description: Optional[str] =None

# SqlAlchemy 모델
# Pydantic 모델: 

# request 요청 모델
class TeacherCreate(TeacherBase):
    pass

# request 응답 모델
class TeacherResponse(TeacherBase):
    id: int
    
#업데이트 할 때 사용되는 모델
class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    is_active: bool
    nickname: Optional[str] = None
    description: Optional[str] =None


# 학생=====================================================

class StudentBase(BaseModel):
    name :str
    lunch_menu : Optional[str] = None
    description: Optional[str] =None


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int
    
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    lunch_menu: Optional[str] = None
    description: Optional[str] =None

