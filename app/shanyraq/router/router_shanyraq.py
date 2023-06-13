from winreg import HKEY_CURRENT_USER
from fastapi import Depends
from app.shanyraq.router.basemodel import ShanyrakCreate

class CreateShanyrakResponse(ShanyrakCreate):
    type: str
    price: float
    address: str
    area: float
    rooms_count: int
    description: str

@router.post("/shanyraks")
def create_shanyrak(
    shanyrak: ShanyrakCreate,
    user_id: str = Depends(HKEY_CURRENT_USER),

):
    shanyrak_dict = shanyrak.dict()
    shanyrak_dict["user_id"] = user_id
    return CreateShanyrakResponse(**shanyrak_dict)
