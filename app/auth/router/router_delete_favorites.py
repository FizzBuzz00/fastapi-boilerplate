from bson import ObjectId
from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.auth.service import Service, get_service
from . import router

@router.delete("/users/favorites/shanyraks/{id:str}")
def delete_favorites_house(
    fav_id:str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service)
):
    svc.repository.remove_favorites(fav_id, jwt_data.user_id)
    return Response(status_code=200)