from typing import Optional
from enum import Enum

from pydantic import BaseModel,Field 

class Twitter(BaseModel):
     last_name:str