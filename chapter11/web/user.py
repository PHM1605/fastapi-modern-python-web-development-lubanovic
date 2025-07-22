import os 
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User 

if os.getenv("CRYPTID_UNIT_TEST"):
  from fake import user as service 
else:
  from service import user as service 
from error import Missing, Duplicate 

ACCESS_TOKEN_EXPIRE_MINUTES = 30

def unauthed():
  raise HTTPException(
    status_code = 401,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"}
  )

router = APIRouter(prefix="/user")

# This dependency makes a POST to "/user/token" (from a form with username & password)
# and returns an access token
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")
@router.post("/token")
async def create_access_token(form_data:OAuth2PasswordRequestForm=Depends()):
  user = service.auth_user(form_data.username, form_data.password)
  if not user:
    unauthed()
  expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = service.create_access_token(
    data={"sub":user.username}, expires=expires
  )
  return {"access_token": access_token, "token_type":"bearer"}

@app.get("/token")
def get_access_token(token:str=Depends(oauth2_dep))->dict:
  return {"token": token}

## CRUD stuffs
@router.get("/")
def get_all() -> list[User]:
  return service.get_all()

@router.get("/{name}")
def get_one(name)->User:
  try:
    return service.get_one(name)
  except Missing as exc:
    raise HTTPException(status_code=404, detail=exc.msg)

@router.post("/", status_code=201)
# 'user' is from request body
def create(user:User)->User: 
  try:
    return service.create(user)
  except Duplicate as exc:
    raise HTTPException(status_code=409, detail=exc.msg)

@router.patch("/")
# 'name' is from query params (not a type) i.e. PATCH /user/?name=alice
# 'user' is from Body
def modify(name:str, user:User)->User:
  try:
    return service.modify(name, user)
  except Missing as exc:
    raise HTTPException(status_code=404, detail=exc.msg)
  
@router.delete("/{name}")
def delete(name:str) -> None:
  try:
    return service.delete(name)
  except Missing as exc:
    raise HTTPException(status_code=404, detail=exc.msg)
    
