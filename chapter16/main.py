from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles 
from pathlib import Path
from fastapi.templating import Jinja2Templates

app = FastAPI()

static_dir = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")
# http -f -b GET localhost:8000/who2 name="Bob Frapples"
# 'f' for 'form'
@app.post("/who2")
def greet2(name:str = Form()):
  return f"Hello, {name}?"

# http://localhost:8000/list 
from fastapi import Request
top = Path(__file__).resolve().parent
template_obj = Jinja2Templates(directory=f"{top}/template")
from fake.creature import _creatures as fake_creatures
from fake.explorer import _explorers as fake_explorers
@app.get("/list")
def explorer_list(request: Request):
  return template_obj.TemplateResponse("list.html",
    {"request": request, "explorers": fake_explorers, "creatures": fake_creatures}
  )