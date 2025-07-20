from fastapi import FastAPI 
from web import explorer 

app = FastAPI()
app.include_router(explorer.router)

@app.get("/")
def top():
    return "top here"

#http -b localhost:8000/echo/argh
@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"
