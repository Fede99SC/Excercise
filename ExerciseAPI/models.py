from fastapi import HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine

class Cat(BaseModel):
    id: int
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

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    age = Column(Integer)
    size = Column(Integer)
    country = Column(String)
    insertedat = Column(DateTime)
    modifiedat = Column(DateTime, nullable=True)

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


def create_cat(db: Session, cat: Cat):
    db_cat = DBCat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)

    return db_cat

def get_cat(db: Session, cat_id: int):
    return db.query(DBCat).where(DBCat.id == cat_id).first()

def get_cats(db: Session):
    return db.query(DBCat).all()

def delete_cat(db: Session, cat_id: int):
    cat_delete = db.get(DBCat, cat_id)
    if not cat_delete:
        raise HTTPException(status_code = 404, detail="Cat not found!")
    db.delete(cat_delete)
    db.commit()
    return{"OK": True}


def update_cat(db: Session, cat_id: int, cat: Cat):
    cat_update = db.query(DBCat).where(DBCat.id == cat_id)
    if not cat_update:
        raise HTTPException(status_code = 404, detail="Cat not found!")
    new_cat = {"name": cat.name, "age": cat.age, "size": cat.size, "country": cat.country}
    cat_update.update(new_cat)
    db.commit()
    db.refresh(new_cat)
    return {"OK": True}


def delete_cat_array(db: Session, cat_id: int):
    cat_delete = db.get(DBCat, cat_id)
    if not cat_delete:
        raise HTTPException(status_code = 404, detail="Cat not found!")
    db.delete(cat_delete)
    db.commit()

    return{"OK": True}

def create_user(db: Session, user: User):

    if db.query(DBUser).where(DBUser.email != user.email).first():
        db_user = DBUser(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return ("User is present!")


def check_user(db: Session, user_email: str, user_password: str):

    if db.query(DBUser).where(DBUser.email == user_email).first() and \
       db.query(DBUser).where(DBUser.password == user_password).first():
        return True
    return False