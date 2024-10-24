from fastapi import APIRouter
from ..usertablemanager import *
from pydantic import BaseModel

import enum
import uuid

class UserLoginModel(BaseModel):
    user:str
    hashedpassword:str

userrouter = APIRouter(
    prefix='/users'
)

@userrouter.post('/getsalt')
def a():
    pass

@userrouter.post('/login')
async def login(UserModel:UserLoginModel):
    try:    
        return f"response: {str(verifylogininfo(UserModel.user, UserModel.hashedpassword, cursor))}"
    except Exception as err:
        print(err)
