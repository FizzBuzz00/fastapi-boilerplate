from pydantic import BaseModel

class ShanyrakCreate(BaseModel):
    type: str
    price: float
    address: str
    area: float
    rooms_count: int
    description: str

class Shanyrak(BaseModel):
    _id: str
    type: str
    price: float
    address: str
    area: float
    rooms_count: int
    description: str
    user_id: str
