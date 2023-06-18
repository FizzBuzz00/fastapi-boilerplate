from typing import Optional
from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from app.auth.service import Service, get_service
from app.utils import AppModel
from . import router

class Res(AppModel):
    shanyraks : list

@router.get("/users/favorites/shanyraks/", response_model=Res)
def get_favorites_house(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service)
):
    getReq = svc.repository.get_favorites(jwt_data.user_id)
    return Res(shanyraks=getReq)