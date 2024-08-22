from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import models
from src import crud, schemas
from src.database import get_db , engine , SessionLocal

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
   
)


@router.get('/')
def main():
    return {"message" : "안녕하세요 여러분 여기는 야삐 서버 입니다"}

@router.post("/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 가입된 이메일 입니다.")

    db_username = crud.get_user_by_username(db, username=user.username)
    if db_username:
        raise HTTPException(status_code=400, detail="사용중인 이름입니다.")
    
    
    return crud.create_user(db=db, user=user)
  
  
@router.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, username=user.username, password=user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="아이디와 비밀번호가 일치하지 않습니다.")
    return {"message" : "로그인 성공!"}


