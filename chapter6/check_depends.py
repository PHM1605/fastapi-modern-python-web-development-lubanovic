# dependencies that don't return values, only CHECK
from fastapi import FastAPI, Depends, Params 

app = FastAPI() 

# dependency function
def check_dep(name:str=Params, password:str=Params):
    if not name:
        raise 

@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user()->bool:
    return True 