from .init import curs, conn, IntegrityError
from model.explorer import Explorer 
from error import Missing, Duplicate

curs.execute("""
  create table if not exists explorer (
    name text primary key,
    country text,
    description text
  )
""")

def row_to_model(row: tuple) -> Explorer:
  return Explorer(name=row[0], country=row[1], description=row[2])

def model_to_dict(explorer: Explorer) -> dict:
  return explorer.dict() if explorer else None 

#  http localhost:8000/explorer/Beau%20Buffete
def get_one(name:str)->Explorer:  
  qry = "select * from explorer where name=:name"
  params = {"name": name}
  curs.execute(qry, params)
  row = curs.fetchone()
  if row:
    return row_to_model(row)
  else: 
    raise Missing(msg=f"Explorer {name} not found")

# http -v localhost:8000/explorer
def get_all() -> list[Explorer]:
  qry = "select * from explorer"
  curs.execute(qry)
  return [row_to_model(row) for row in curs.fetchall()]

#  http post localhost:8000/explorer/ name="Beau Buffete" country="US" description="" 
def create(explorer: Explorer) -> Explorer:
  qry = """
    insert into explorer(name, country, description) 
    values (:name, :country, :description)"""
  params = model_to_dict(explorer)
  try:
    curs.execute(qry, params)
  except IntegrityError:
    raise Duplicate(msg=f"Explorer {explorer.name} already exists")
  conn.commit()
  return get_one(explorer.name)

def modify(name: str, explorer: Explorer) -> Explorer:
  qry = """
    update explorer
    set country=:country, name=:name, description=:description
    where name=:name_orig"""
  params = model_to_dict(explorer)
  params["name_orig"] = name 
  curs.execute(qry, params)
  conn.commit()
  if curs.rowcount == 1:
    return get_one(explorer.name)
  else:
    raise Missing(msg=f"Explorer {name} not found") 

def delete(name:str):
  if not name: 
    raise Missing(msg="Empty name")
  qry = "delete from explorer where name=:name"
  params = {"name": name}
  res = curs.execute(qry, params)
  if curs.rowcount != 1:
    raise Missing(msg=f"Explorer {name} not found")
  conn.commit()
  return bool(res)
