import os
from fastapi import APIRouter, HTTPException, Query, Path
from model.creature import Creature 
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service 
else:
    from service import creature as service 
from error import Missing, Duplicate 

router = APIRouter(prefix="/creature")

@router.get("/")
def get_all()->list[Creature]:
	return service.get_all()

@router.get("/{name}", responses={404: {"description":"Creature not found"}})
def get_one(name: str) -> Creature:
	try:
		return service.get_one(name)
	except Missing as exc:
		raise HTTPException(status_code=404, detail=exc.msg)

@router.post("/", responses={409: {"description":"Creature already exists"}})
def create(creature: Creature) -> Creature:
	try:
		return service.create(creature)
	except Duplicate as exc:
		raise HTTPException(status_code=409, detail=exc.msg)

@router.patch("/{name}", responses={404:{"description":"Creature not found"}})
def modify(creature: Creature, name:str=Path(...,min_length=2)) -> Creature:
	try:
		return service.modify(name, creature)
	except Missing as exc:
		raise HTTPException(status_code=404, detail=exc.msg)

@router.put("/{name}")
def replace(name:str, creature: Creature) -> Creature:
	return service.replace(name, creature)
	
@router.delete("/{name}", 
	responses={
		200: {"description": "Creature deleted"},
		404: {"description": "Creature not found"},
		422: {"description": "Validation error"}
	})
def delete(name: str=Path(..., min_length=2)):
	try:
		service.delete(name)
		return {"message": f"Creature '{name}' deleted"}
	except Missing as exc:
		raise HTTPException(status_code=404, detail=exc.msg)
        