from faker import Faker 
from time import perf_counter
from error import Duplicate
from data.explorer import create, get_all
from model.explorer import Explorer
from main import app 
from fastapi.testclient import TestClient 

def load():
  f = Faker()
  NUM = 100
  t1 = perf_counter()
  for row in range(NUM):
    try:
      create(Explorer(name=f.name(), country=f.country(), description=f.text()))
    except Duplicate:
      pass 
  t2 = perf_counter()
  print(NUM, "rows")
  print("write time:", t2-t1)

def read_db():
  t1 = perf_counter()
  _ = get_all()
  t2 = perf_counter()
  print("db read time:", t2-t1)

def read_api():
  t1 = perf_counter()
  client = TestClient(app)
  _ = client.get("/explorer/")
  t2 = perf_counter()
  print("api read time:", t2-t1)

load()
read_db()
read_db()
read_api()
