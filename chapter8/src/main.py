from fastapi import FastAPI 
from web import explorer, creature
# run with: python -m main
app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)
