from fastapi import FastAPI 
from web import user

app = FastAPI()
app.include_router(user.router)
