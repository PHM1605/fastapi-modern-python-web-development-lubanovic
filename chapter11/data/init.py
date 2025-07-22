import os
from pathlib import Path 
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection|None = None 
curs = Cursor|None = None 

def get_db(name:str|None=None, reset:bool=False):
  global conn, curs 
  if conn:
    if not reset:
      return 
    conn = None 
  if not name:
    name = os.getenv('CRYPTID_SQLITE_DB')
    topdir = Path(__file__).resolve().parents[1] # 'chapter11' folder
    db_dir = topdir/"db"
    db_name = "cryptid.db"
    db_path = str(db_dir/db_name)
    name = os.getenv("CRYPTID_SQLITE_DB", db_path) # chapter11/db/cryptid.db
  conn = connect(name, check_same_thread=False)
  curs = conn.cursor()

get_db()