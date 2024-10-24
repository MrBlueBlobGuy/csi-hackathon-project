from fastapi import APIRouter

userrouter = APIRouter(
    prefix='/users'
)

@userrouter.post('/getsalt')
def a():
    pass

@userrouter.post('/login')
async def login(user:str, hashedpassword):
    pass