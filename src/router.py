from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from src import models
from src import crud, schemas
from src.database import get_db , engine , SessionLocal

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
   
)


@router.get("/", response_class=HTMLResponse)
def main():
    html_content = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>야삐 서버</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #4CAF50;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>안녕하세요 여러분</h1>
            <p>여기는 야삐 서버 입니다</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 가입된 이메일 입니다.")

    db_username = crud.get_user_by_username(db, username=user.username)
    if db_username:
        raise HTTPException(status_code=400, detail="사용중인 이름입니다.")
    
    
    return crud.create_user(db=db, user=user)
  
  
@router.post("/signin")
def signin(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, username=user.username, password=user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="아이디와 비밀번호가 일치하지 않습니다.")
    return {"message" : "로그인 성공!"}


