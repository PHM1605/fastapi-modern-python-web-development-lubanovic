from fastapi import FastAPI, Depends, Params

app = FastAPI()

# dependency: receive username&password, return True if valid
def user_dep(name:str=Params, password:std=Params):
    return {"name":name, "valid":True}

# user: {"name":"abc", "valid":True}
@app.get("/user")
def get_user(user:dict = Depends(user_dep)) -> dict:
    return user 
