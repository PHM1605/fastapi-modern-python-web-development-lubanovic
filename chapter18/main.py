from fastapi import FastAPI 
from web import game 

app = FastAPI()

app.include_router(game.router)
