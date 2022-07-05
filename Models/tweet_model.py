from typing import Optional
from enum import Enum
from datetime import date,datetime
from Models.user_model import UserBase
from uuid import UUID

from pydantic import BaseModel,Field 

class Tweet(BaseModel):
     Tweet_id: UUID = Field(...)
     content:str = Field(...,max_length=256,min_length=1)
     created_at:date = Field(default=datetime.now())
     update_at:Optional[date] = Field(default=datetime.now())
     by:UserBase =Field(...)