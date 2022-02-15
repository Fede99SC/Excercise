from fastapi import HTTPException

from sqlalchemy.orm import Session
from models import DBCat, Cat, User, DBUser


def create_cat(db: Session, cat: Cat):
    db_cat = DBCat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)

    return db_cat

def get_cat(db: Session, cat_id: int):

    if db.query(DBCat).where(DBCat.id == cat_id).first():
        return db.query(DBCat).where(DBCat.id == cat_id).first()
    else:
        raise HTTPException(status_code = 404, detail="Cat not found!")

def get_cats(db: Session):
    return db.query(DBCat).all()

def delete_cat(db: Session, cat_id: int):
    cat_delete = db.get(DBCat, cat_id)
    if not cat_delete:
        raise HTTPException(status_code = 404, detail="Cat not found!")
    db.delete(cat_delete)
    db.commit()

    return{"OK": True}


def update_cat(db: Session, cat: Cat):
    update_cat = {"name": cat.name, "age": cat.age, "size": cat.size, "country": cat.country}
    db_result=db.query(DBCat).filter(DBCat.id == cat.id)
    if(db_result.first()):
        print('ok')
        db_result.update(update_cat)
        db.commit()
        return update_cat
    raise HTTPException(status_code=400, detail="Cat not found!")

    #raise HTTPException(status_code = 404, detail="Cat not found!")


def delete_cat_array(db: Session, cat_id: int):
    cat_delete = db.get(DBCat, cat_id)
    if not cat_delete:
        raise HTTPException(status_code = 404, detail="Cat not found!")
    db.delete(cat_delete)
    db.commit()

    return{"OK": True}

def create_user(db: Session, user: User):

    try:
        db_user = DBUser(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except:
        raise HTTPException(status_code = 400, detail="User is present!")


def check_user(db: Session, user_email: str, user_password: str):

    if db.query(DBUser).where(DBUser.email == user_email).first() and \
            db.query(DBUser).where(DBUser.password == user_password).first():
        return True
    else:
        raise HTTPException(status_code=400, detail="User not found or Email or Password not correct!")

