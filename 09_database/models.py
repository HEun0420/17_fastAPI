from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean

# String => 고정된 길이(길이제한)
# Text => 길이제한이 없다. 

class Teacher(Base):
    __tablename__ = 'teachers'
    
    # 컬럼 설정
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    is_active = Column(Boolean, default= True)
    description= Column(Text)
    
    
# =================================================

class Student(Base):
    __tablename__ = 'students' 

    # 컬럼 설정
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    lunch_menu = Column(String(50))
    description= Column(Text)
    
# 관계설정 기능 (ex. 일대다로 묶기)