from pydantic import BaseModel, constr

class Explorer(BaseModel):
    name: constr(min_length=1) 
    country: str 
    description: str 
    