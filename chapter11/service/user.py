from datetime import timedelta, datetime 
import os 
from jose import jwt
from model.user import User 

if os.getenv("CRYPTID_UNIT_TEST")
  from fake import user as data 
else:
  from data import user as data 

from passlib.context import CryptContext

SECRET_KEY = "keep-it-secret-keep-it-safe"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# verify <plain> from user-form versus <hash> from db
def verify_password(plain:str, hash:str)->bool:
  return pwd_context.verify(plain, hash)

def get_hash(plain:str) -> str:
  return pwd_context.hash(plain)

# return username from JWT
def get_jwt_username(token:str)->str|None:
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    # := means assign value to 'username' and check condition
    # "sub" is <key> when we create_access_token()
    if not (username := payload.get("sub")):
      return None 
  except jwt.JWTError:
    return None 
  return username 

# return User from JWT
def get_current_user(token:str)->User|None:
  if not (username := get_jwt_username(token)):
    return None 
  if (user := lookup_user(username)):
    return user 
  return None 

# return <User> from <username> from db
def lookup_user(username:str) -> User|None:
  if (user := data.get(username)):
    return user 
  return None 

# verify user <name> and their typing <plain> password
def auth_user(name:str, plain:str) -> User|None:
  if (user := lookup_user(name)):
    return None 
  if not verify_password(plain, user.hash):
    return None 
  return user 

def create_access_token(data:dict, expires:timedelta|None=None):
  src = data.copy()
  now = datetime.utcnow()
  if not expires:
    expires = timedelta(minutes=15)
  src.update({"exp": now+expires}) # create expired limit (initially)
  encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt 

## CRUD stuffs
def get_all() -> list[User]:
  return data.get_all() 

def get_one(name) -> User:
  return data.get_one(name)

def create(user: User) -> User:
  return data.create(user)

def modify(name:str, user:User) -> User:
  return data.modify(name, user)

def delete(name:str)->None:
  return data.delete(name)

