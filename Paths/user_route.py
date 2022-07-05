# python
from typing import Optional,List
from enum import Enum

# pydantic
from pydantic import BaseModel, Field

# checar los mas importantes para validarlos
from pydantic import NameEmail, EmailStr
# fastapi
from fastapi import Cookie, APIRouter, Body, Form, Header, Query, Path,UploadFile,File,status
from fastapi import HTTPException

# # importar los Models
from Models.user_model import UserBase,UserComplete

router = APIRouter()


## Users

@router.post(
    path =('/signup'),
    response_model=UserBase,
    status_code=status.HTTP_201_CREATED,
    summary='Register User',
    tags = ['Users']
)
def signup():
    pass


@router.post(
    path =('/login'),
    response_model=UserBase,
    status_code=status.HTTP_200_OK,
    summary='Login User',
    tags = ['Users']
)
def login():
    pass


@router.get(
    path =('/users'),
    response_model=List[UserBase], #List viene de Typing
    status_code=status.HTTP_200_OK,
    summary='show all Users',
    tags = ['Users']
)
def show_all_users():
    pass


@router.get(
    path =('/users/{user_id}'),
    response_model=UserBase, #List viene de Typing
    status_code=status.HTTP_200_OK,
    summary='show User',
    tags = ['Users']
)
def show_user():
    pass

@router.delete(
    path =('/users/{user_id}/delete'),
    response_model=UserBase,
    status_code=status.HTTP_200_OK,
    summary='delete User',
    tags = ['Users']
)
def delete_user():
    pass


@router.put(
    path =('/users/{user_id}/update'),
    response_model=UserBase,
    status_code=status.HTTP_200_OK,
    summary='update User',
    tags = ['Users']
)
def delete_user():
    pass
# @router.post(path="/getuser",response_model=Twitter,status_code=status.HTTP_200_OK)
# def create_person(user: Twitter = Body(...)):
#     return user