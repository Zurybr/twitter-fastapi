
# python
from typing import Optional,List
from enum import Enum
import json
from uuid import uuid4

# pydantic
from pydantic import BaseModel, Field

# checar los mas importantes para validarlos
from pydantic import NameEmail, EmailStr
# fastapi
from fastapi import Cookie, APIRouter, Body, Form, Header, Query, Path,UploadFile,File,status
from fastapi import HTTPException

# # importar los Models
from Models.tweet_model import Tweet

router = APIRouter()


## Tweet
@router.post(
    path =('/Tweets/create'),
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Create a new tweet',
    tags = ['Tweets']
)
def create_tweet(tweet:Tweet = Body(...)):
    """
    Create_tweet: Register an user in the app

    Parameters:
        -Request body parameter
            -user:UserComplete
    
    Returns a Json with the basic information
        -user_id: UUID
        -email: Emailstr
        -first_name:str
        -birth_date:date
    """
    with open("./Data/tweets.json",'r+',encoding='utf8') as f:
        result = json.loads(f.read())
        tweet_dict = tweet.dict() #metodo interno de fastapi body para convertir request body a dictionario
        tweet_dict['user_id']=str(uuid4())
        tweet_dict['birth_date']=str(tweet_dict['birth_date'])
        print(tweet_dict)
        result.append(tweet_dict)
        f.seek(0)#moverme al byte 0
        f.write(json.dumps(result))
    return(tweet_dict)


@router.get(
    path =('/Tweets'),
    response_model=List[Tweet], #List viene de Typing
    status_code=status.HTTP_200_OK,
    summary='show all Tweets',
    tags = ['Tweets']
)
def show_all_Tweets():
    pass


@router.get(
    path =('/Tweets/{user_id}'),
    response_model=Tweet, #List viene de Typing
    status_code=status.HTTP_200_OK,
    summary='show User',
    tags = ['Tweets']
)
def show_user():
    pass


@router.delete(
    path =('/Tweets/{user_id}/delete'),
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='delete User',
    tags = ['Tweets']
)
def delete_user():
    pass


@router.put(
    path =('/Tweets/{user_id}/update'),
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='update User',
    tags = ['Tweets']
)
def delete_user():
    pass
