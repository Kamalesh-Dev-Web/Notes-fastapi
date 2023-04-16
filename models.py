from beanie import Document
from pydantic import BaseModel,Field
from typing import Union,Optional
from datetime import datetime


class Note(Document):
    title:Union[str, None]=Field(max_length=400)
    created_date:Union[datetime,None]
    updated_date:Union[datetime,None]
    is_completed:Union[bool,None]
   
    
    class Settings:
        name="notes_database"
    
    class Config:
        schema_extra={
             "title":"Avengers",
             "created_date":"9.0",
             "updated_date":2001,
             "is_completed":True,
            
        }


class UpdateNote(BaseModel):
    title:Optional[str]=None
    created_date:Optional[datetime]=None
    updated_date:Optional[datetime]=None
    is_completed:Optional[bool]=None