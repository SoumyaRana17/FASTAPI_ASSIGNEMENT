from pydantic import BaseModel,Field
from enum import Enum
from sqlmodel import SQLModel

class location_of_obj(str,Enum):
    ELECTRONICS="ELECTRONICS"
    DOCUMENTS="DOCUMENTS"
    ACESSORIES="ACESSORIES"
    STATIONARY="STATIONARY"
    OTHER="OTHER"
class status_of_obj(str,Enum):
    LOST="LOST"
    FOUND="FOUND"
    RETURNED="RETURNED"
class item(SQLModel):
    
    title:str=Field(min_length=1)
    description: str = Field(min_length=1)
    category:location_of_obj=Field(default=location_of_obj.OTHER)
    location:str
    reported_by:str
    status:status_of_obj=Field(default=status_of_obj.LOST)

class item_update(SQLModel):
    status:status_of_obj=Field(default=status_of_obj.LOST)

    