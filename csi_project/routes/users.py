from fastapi import APIRouter
from ..usertablemanager import *
from pydantic import BaseModel

import uuid
import json

class UserLoginModel(BaseModel):
    user:str
    hashedpassword:str

class UserSignupModel(BaseModel):
    username:str
    hashedsaltedpassword:str
    salt:str
    usertype:int

userrouter = APIRouter(
    prefix='/users'
)

@userrouter.get('/getsalt')
def getsalt(username):
    return getsaltfromdb(username, cursor)

@userrouter.post('/login')
async def login(UserModel:UserLoginModel):
    try:    
        return json.dumps({"response": str(verifylogininfo(UserModel.user, UserModel.hashedpassword, cursor))})
    except Exception as err:
        print(err)

@userrouter.get("/generatenewsalt")
def generatenewsalt():
    id = uuid.UUID()
    return "{}"

@userrouter.post("/signup")
def signup(signupmodel:UserSignupModel):
    add_entry(signupmodel.username, signupmodel.hashedsaltedpassword, str(uuid.UUID()))

