# python
from typing import Optional,List
from enum import Enum
import json #trabajar con archivos json
from uuid import uuid4

# pydantic
from pydantic import  BaseModel, Field

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
def signup(user:UserComplete = Body(...)):
    """
    SignUp: Register an user in the app

    Parameters:
        -Request body parameter
            -user:UserComplete
    
    Returns a Json with the basic information
        -user_id: UUID
        -email: Emailstr
        -first_name:str
        -birth_date:date
    """
    with open("./Data/users.json",'r+',encoding='utf8') as f:
        result = json.loads(f.read())
        user_dict = user.dict() #metodo interno de fastapi body para convertir request body a dictionario
        user_dict['user_id']=str(uuid4())
        user_dict['birth_date']=str(user_dict['birth_date'])
        print(user_dict)
        result.append(user_dict)
        f.seek(0)#moverme al byte 0
        f.write(json.dumps(result))
    return(user_dict)



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
    """
    Getall: Show all users

    Parameters:
        -None
    
    Returns a Json with all user in the app
        -user_id: UUID
        -email: Emailstr
        -first_name:str
        -birth_date:date
    """
    with open("./Data/users.json",'r',encoding='utf8') as f:
        result = json.loads(f.read())
        return result


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


#files

@router.post(
    path = '/post-image'
)
def post_image(
    image:UploadFile = File(...)
):
    return{
        'Filename': image.filename,
        "Format":image.content_type,
        "Size (kb)": round(len(image.file.read())/1024,ndigits=2)
    }
