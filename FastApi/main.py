from fastapi import FastAPI

#For JSON objects
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
def getAllValues():
    return {"message": "Hello World"}

@app.get("/param/{param_name}")
def getAllValuesByParam(param_name:str):
    #Data validation Handling With pydantic
    return {"message",param_name}

#Using pydantic to declare JSON objects
@app.post("/items/")
async def create_item(item: Item):
    return item

#To run this use below command
# uvicorn main:app --reload