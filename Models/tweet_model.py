from typing import Optional
from enum import Enum
from datetime import date,datetime
from Models.user_model import UserBase
from uuid import UUID

from pydantic import BaseModel,Field 

class Tweet(BaseModel):
     tweet_id:Optional[UUID] = Field(default=None)
     content:str = Field(...,max_length=256,min_length=1)
     created_at: datetime = Field(default=datetime.now())
     updated_at: Optional[datetime] = Field(default=None)
     by: UserBase = Field(...)