from fastapi import APIRouter 
from model.explorer import Explorer 
import data.explorer as service 

router = APIRouter(prefix="/explorer")

# http -v localhost:8000/explorer
@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer|None:
    return service.get_one(name)

# http post localhost:8000/explorer/ name="Beau Buffete", country="US", description=""
@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

# http -b PATCH localhost:8000/explorer/ name="Noah Weiser" country="DE" description="Myoptic machete man"
@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    return service.modify(explorer)

# http -b PUT localhost:8000/explorer/ name="Noah Weiser" country="DE" description="Myoptic machete man"
@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)

# http -b DELETE localhost:8000/explorer/Noah%20Weiser
# http -b DELETE localhost:8000/explorer/Edmund%20Hillary
@router.delete("/{name}")
def delete(name: str): 
    if name == "Noah Weiser":
        return True
    else:
        return False
