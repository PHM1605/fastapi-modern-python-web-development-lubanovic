from fastapi import APIRouter 

router = APIRouter(prefix="/explorer")

@router.get("/")
def top():
    print("ABNC")
    return "top explorer endpoint"