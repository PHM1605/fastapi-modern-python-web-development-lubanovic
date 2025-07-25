from pathlib import Path 
from fastapi import APIRouter, Body, Request 
from fastapi.templating import Jinja2Templates
from service import game as service 

router = APIRouter(prefix="/game")
@router.get("")
def game_start(request:Request):
  name = service.get_word()
  top = Path(__file__).resolve().parents[1] # 'chapter18'
  templates = Jinja2Templates(directory=f"{top}/template")
  return templates.TemplateResponse("game.html", {"request":request, "word":name})

# Subsequent game requests
@router.post("")
async def game_step(word:str=Body(), guess:str=Body()):
  score = service.get_score(word, guess)
  return score # "MMHMCMM" (M=Miss, H=Hit, C=Close)
