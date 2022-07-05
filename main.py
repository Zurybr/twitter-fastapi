# python
from typing import Optional
from enum import Enum

# pydantic
from pydantic import BaseModel, Field

# checar los mas importantes para validarlos
from pydantic import NameEmail, EmailStr
# fastapi
from fastapi import Cookie, FastAPI, Body, Form, Header, Query, Path,UploadFile,File,status
from fastapi import HTTPException
# # importar los Models
from Models.user_model import UserBase,UserComplete
from Models.twitter_model import Twitter

app = FastAPI()

@app.get(path='/')
def home():
    return {'work':'it'}

@app.post(path="/getuser",response_model=UserBase,status_code=status.HTTP_200_OK)
def create_person(user: UserBase = Body(...)):
    return user