from fastapi import FastAPI 
from web import user
# run with: python -m uvicorn main:app --reload

app = FastAPI()
app.include_router(user.router)
