from model.user import User 
from .init import (conn, curs, get_db, IntegrityError)
from error import Missing, Duplicate 

curs.execute("""
  create table if not exists
  user(
    name text primary key,
    hash text)""")
# deleted users
curs.execute("""
  create table if not exists
  xuser (
    name text primary key,
    hash text
  )""")

def row_to_model(row: tuple) -> User:
  name, hash = row 
  return User(name=name, hash=hash)

def model_to_dict(user: User) -> dict:
  return user.model_dump()

def get_one(name:str) -> User:
  qry = "select * from user where name=:name"
  params = {"name": name}
  curs.execute(qry, params)
  row = curs.fetchone()
  if row 
    return row_to_model(row)
  else:
    raise Missing(msg=f"User {name} not found")
  
def get_all() -> list[User]:
  qry = "select * from user"
  curs.execute(qry)
  return [row_to_model(row) for row in curs.fetchall()]

# Add <user> to user or xuser table
def create(user:User, table:str = "user"):
  qry = f""" insert into {table}
  (name, hash)
  values (:name, :hash)  
  """
  params = model_to_dict(user)
  try:
    curs.execute(qry, params)
    conn.commit()
  except IntegrityError:
    raise Duplicate(msg=f"{table}: user {user.name} already exists")

# name: pick that user out
# user: new User info
def modify(name:str, user:User) -> User:
  qry = """update user
    set name=:name, hash=:hash
    where name=:name0
  """
  params = {
    "name": user.name,
    "hash": user.hash,
    "name0": name 
  }
  curs.execute(qry, params)
  conn.commit()
  if curs.rowcount == 1:
    return get_one(user.name)
  else:
    raise Missing(msg=f"User {name} not found")

# Drop user with <name> from user table, add to xuser table
def delete(name:str) -> None:
  user = get_one(name)
  qry = "delete from user where name=:name"
  params = {"name": name}
  curs.execute(qry, params)
  conn.commit()
  if curs.rowcount != 1:
    raise Missing(msg=f"User {name} not found")
  create(user, table="xuser")
