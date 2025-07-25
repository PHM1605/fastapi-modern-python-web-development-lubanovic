import os
from fastapi import APIRouter, HTTPException, Query, Path
from model.creature import Creature 
if os.getenv("CRYPTID_UNIT_TEST"):
	print("use fake data")
	from fake import creature as service 
else:
	print("use real data")
	from service import creature as service 
from error import Missing, Duplicate 

router = APIRouter(prefix="/creature")

@router.get("/")
def get_all()->list[Creature]:
	return service.get_all()

## --------------------- for plotly test -----------------------------------
# http://localhost:8000/creature/test
from fastapi import Response 
import plotly.express as px 

@router.get("/test")
def test():
	df = px.data.iris() # columns: sepal_length, sepal_width, ..., species, species_id
	fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
	fig_bytes = fig.to_image(format="png")
	return Response(content=fig_bytes, media_type="image/png")
## --------------------------------------------------------------------------

## ------------------- for barchart with creature initials ------------------
# http://localhost:8000/creature/plot
from collections import Counter 
import plotly.express as px 
from service.creature import get_all 
@router.get("/plot")
def plot():
	creatures = get_all()
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	counts = Counter(creature.name[0] for creature in creatures)
	y = {letter: counts.get(letter) for letter in letters}
	fig = px.histogram(x=list(letters), y=y, title="Creature Names", labels={"x":"Initial", "y":"Initial"}) # y label automatically converted to "Sum pf Initial"
	fig_bytes = fig.to_image(format="png")
	return Response(content=fig_bytes, media_type="image/png")
## --------------------------------------------------------------------------

## ------------------- show a map of origin country of creatures ------------------
# http://localhost:8000/creature/map
import country_converter as coco 
@router.get("/map")
def map():
	creatures = service.get_all()
	iso2_codes = set(creature.country for creature in creatures) # country code with 2 chars
	iso3_codes = coco.convert(names=iso2_codes, to="ISO3") # country code with 3 chars
	fig = px.choropleth(
		locationmode="ISO-3",
		locations=iso3_codes,
		title="Cryptids by Country",
	)
	fig_bytes = fig.to_image(format="png")
	return Response(content=fig_bytes, media_type="image/png")

# def map():
# 	creatures = service.get_all()
# 	us_state_codes = [c.area for c in creatures if c.country == "US" and c.area.strip()]
	
# 	fig = px.choropleth(
# 			locations=us_state_codes,
# 			locationmode="USA-states",  # USA states instead of ISO-3 countries
# 			scope="usa",                # zoom to USA
# 			title="Cryptids by US State",
# 	)
# 	fig_bytes = fig.to_image(format="png")
# 	return Response(content=fig_bytes, media_type="image/png")	
## --------------------------------------------------------------------------

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
        
