from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

# basic
@app.get("/hi")
def greet():
    return "Hello? World?"

# # 'who' is part of the link
# @app.get("/hi/{who}")
# def greet(who):
#     return f"Hello? {who}?"

# # assuming 'who' is a query params
# # http -b localhost:8000/hi?who=Mom
# # http -b localhost:8000/hi who==Mom
# @app.get("/hi")
# def greet(who):
#     return f"Hello? {who}?"

# http -v localhost:8000/hi who=Dad
# "=" means we gives the json {"who":"Dad"} in Body 
@app.post("/hi")
def greet(who:str=Body(embed=True)):
    return f"Hello? {who}?"

# # http -v POST localhost:8000/hi who:Dad
# # ":" means Header "who" has the value "Dad"
# @app.post("/hi")
# def greet(who:str=Header()):
#     return f"Hello? {who}?"

# Header "User-Agent" converts to variable name "user_agent"
# http -v localhost:8000/agent
@app.get("/agent")
def get_agent(user_agent:str=Header()):
    return user_agent 

@app.get("/happy")
def happy(status_code=200):
    return ":)"

# injecting headers in response
# http localhost:8000/header/marco/polo
@app.get("/header/{name}/{value}")
def header(name:str, value:str, response:Response):
    response.headers[name] = value 
    return "normal body"