from pydantic import BaseModel, constr

class Creature(BaseModel):
    name: constr(min_length=1) 
    country: str 
    area: str 
    description: str 
    aka: str 
    