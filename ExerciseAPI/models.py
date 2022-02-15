from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime
from database import Base, SessionLocal, engine


class Cat(BaseModel):
    name: str
    age: int
    size: int
    country: str
    insertedat: datetime
    modifiedat: Optional[datetime] = None

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DBCat(Base):
    __tablename__ = "Cat"

    id = Column(Integer, primary_key=True, index=True, unique=True,autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    size = Column(Integer)
    country = Column(String)
    insertedat = Column(DateTime(timezone=True))
    modifiedat = Column(DateTime(timezone=True), nullable=True)

class User(BaseModel):
    email: str
    fullname: str
    password: str

    class Config:
        orm_mode = True

class DBUser(Base):
    __tablename__ = "User"

    email = Column(String, primary_key=True, index=True, unique=True)
    fullname = Column(String)
    password = Column(String)

Base.metadata.create_all(bind=engine)
