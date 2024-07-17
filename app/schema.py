from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: str
    email: str

    class Config:
        ffrom_attributes = True
