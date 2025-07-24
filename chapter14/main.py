from fastapi import FastAPI 
from web import explorer, creature
# run with: python -m uvicorn main:app --reload
app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)

## To test: schemathesis run http://localhost:8000/openapi.json