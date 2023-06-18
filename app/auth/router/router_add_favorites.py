from bson import ObjectId
from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.auth.service import Service, get_service
from . import router

@router.post("/users/favorites/shanyraks/{id:str}")
def favorites_house(
    house_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service)
):
    re = svc.repository.get_only_address(house_id)
    svc.repository.add_favorites_house({"shanyraks" : re, "user_id": ObjectId(jwt_data.user_id)})
    return Response(status_code=200)