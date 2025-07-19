from pydantic import BaseModel, constr, Field

# class Creature(BaseModel):
#     name: constr(min_length=2) 
#     country: str 
#     area: str 
#     description: str 
#     aka: str 

class Creature(BaseModel):
    name: str = Field(..., min_length=2) # ... means "required"
    country: str 
    area: str 
    description: str 
    aka: str 

# bad_creature = Creature(name="!", description="it's", area="yourantic")