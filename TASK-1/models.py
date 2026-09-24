from sqlmodel import Field
from schemas import item,location_of_obj,status_of_obj
from sqlmodel import SQLModel
class Item(item, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    



class item(SQLModel):
    id:int
    title:str
    description:str
    category:location_of_obj=Field(default=location_of_obj.OTHER)
    location:str
    status:status_of_obj=Field(default=status_of_obj.LOST)