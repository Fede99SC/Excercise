from main import app
from fastapi import Depends
from typing import List
import uvicorn
from fastapi import FastAPI, Body, Depends
from sqlalchemy.orm import Session
from models import Cat, get_db, User

from dal import get_cat, create_cat, delete_cat, delete_cat_array, update_cat,get_cats,\
create_user, check_user
from auth.jwt_bearer import jwtBearer
from auth.jwt_handler import sign_JWT

#app = FastAPI()


@app.get("/test")
def test():
    return "hello world"


@app.post("/create-cat", response_model=Cat, dependencies=[Depends(jwtBearer())])
def create_cat_view(cat: Cat, db: Session = Depends(get_db)):
    db_cat = create_cat(db, cat)
    return db_cat

@app.get("/information-cat/{cat_id}", dependencies=[Depends(jwtBearer())])
def get_cat_view(cat_id: int, db: Session = Depends(get_db)):
    return get_cat(db, cat_id)

@app.get("/information-cats", response_model=List[Cat], dependencies=[Depends(jwtBearer())])
def get_cats_view(db: Session = Depends(get_db)):
    return get_cats(db)

@app.put("/update-cat")#,dependencies=[Depends(jwtBearer())])
def update_cat_view(cat: Cat, db: Session = Depends(get_db)):
    return update_cat(db, cat)

@app.delete("/delete-cat/{cat_id}", status_code=201,dependencies=[Depends(jwtBearer())])
def delete_cat_view(cat_id: int, db: Session = Depends(get_db)):
    return delete_cat(db, cat_id)

"""
@app.delete("/delete-cat-array/{cat_id}", response_model=List[Cat], dependencies=[Depends(jwtBearer())])
def delete_cats_view(cat_id: int, db: Session = Depends(get_db)):
    return delete_cat_array(db, cat_id)
"""

#-------------User----------------#

@app.post("/user/signup", response_model=User)
def user_signup(user: User, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@app.post("/user/login/")
def user_login(user_email: str, user_password: str, db: Session = Depends(get_db)):
    if check_user(db, user_email, user_password):
        return sign_JWT(user_email)


"""""
if __name__ == "__main__":
    body = Body(default=None)
    uvicorn.run(app, host="0.0.0.0", port=8005)
"""""