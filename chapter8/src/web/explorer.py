from fastapi import APIRouter , HTTPException
from model.explorer import Explorer 
import data.explorer as service 
from error import Duplicate, Missing

router = APIRouter(prefix="/explorer")

# http -v localhost:8000/explorer
@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
  return service.get_all()

# http localhost:8000/explorer/"Beau Buffalo"
@router.get("/{name}")
def get_one(name) -> Explorer:
	try:
		return service.get_one(name)
	except Missing as exc:
		raise HTTPException(status_code=404, detail=exc.msg)

# http post localhost:8000/explorer/ name="Beau Buffete", country="US", description=""
@router.post("")
@router.post("/")
def create(explorer: Explorer) -> Explorer:
	try:
		return service.create(explorer) 
	except Duplicate as exc:
		raise HTTPException(status_code=404, detail=exc.msg)

# http -b PATCH localhost:8000/explorer/ name="Noah Weiser" country="DE" description="Myoptic machete man"
@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
	try:
		return service.modify(explorer)
	except Missing as exc:
		raise HTTPException(status_code=404, detail=exc.msg)

# http -b PUT localhost:8000/explorer/ name="Noah Weiser" country="DE" description="Myoptic machete man"
@router.put("/")
def replace(explorer: Explorer) -> Explorer:
	try:
		service.replace(explorer)
	except Missing as exc:
		raise HTTPException(status_code=404, detail=exc.msg)

# http -b DELETE localhost:8000/explorer/Noah%20Weiser
# http -b DELETE localhost:8000/explorer/Edmund%20Hillary
# http delete localhost:8000/explorer/Beau%20Buffete,
@router.delete("/{name}")
def delete(name: str): 
	try:
		service.delete(name)
	except Missing as exc:
		raise HTTPException(status_code=404, detail=exc.msg)

