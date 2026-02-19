from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel, EmailStr

from typing import Any
app = FastAPI()

class ModelName(str, Enum):
    alexnet= "alexnet"
    resenet= "resenet"
    lenet= "lenet"

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.get("/users/me")
async def read_users_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": "alexnet", "message": "Deep Learning FTW"}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

class Item(BaseModel):
    name:str
    description: str | None= None
    price: float
    tax: float | None=None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user