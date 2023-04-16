from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

from notes import notes_router
from mangum import Mangum
from database import init_db


app = FastAPI()
handler=Mangum(app)


app.include_router(notes_router,prefix='/notes')

@app.on_event('startup')
async def connect():
    await init_db()

# class Item(BaseModel):
#     name:str
#     price:float
#     is_offer:Union[bool,None]=None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}