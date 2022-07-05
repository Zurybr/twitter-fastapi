from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import date

from pydantic import BaseModel,Field,EmailStr

class UserBase(BaseModel):
     user_id: Optional[UUID] = Field(default=None)
     name:str = Field(...,max_length=50,min_length=1)
     last_name:Optional[str] = Field(max_length=50,min_length=1,default=None)
     birth_date: Optional[date]=Field(default=None)

class UserComplete(UserBase):
     email:EmailStr =Field(...,example= 'test.test@test.com')
     password:str = Field(...,min_length=1,max_length=40)
     