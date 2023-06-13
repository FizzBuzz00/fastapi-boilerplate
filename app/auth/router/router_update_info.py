from fastapi import Depends, status
from . import router
from ..adapters.jwt_service import JWTData
from .dependencies import parse_jwt_user_data
from app.auth.service import Service, get_service
from app.utils import AppModel


class UpdateUserInfoRequest(AppModel):
    phone : str
    name : str
    city : str


class UpdateUserInfoResponse(AppModel):
    name: str

@router.patch("/users/me", response_model=UpdateUserInfoResponse)
def update_user_info_method(
    input: UpdateUserInfoRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> status.HTTP_200_OK:
    svc.repository.update_user_info(jwt_data.user_id, input.dict())
    return UpdateUserInfoResponse(name=input.name)