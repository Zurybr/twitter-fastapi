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
# from models import Person

app = FastAPI()

@app.get(path='/')
def home():
    return {'work':'it'}