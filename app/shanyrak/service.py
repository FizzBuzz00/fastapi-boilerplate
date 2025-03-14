
from pydantic import BaseSettings
from app.config import database
from app.shanyrak.adapters.here_service import HereService
from .adapters.s3_service import S3Service

from .repository.repository import ShanyrakRepository


class Config(BaseSettings):
    HERE_API_KEY : str
    AWS_ACCESS_KEY_ID:str
    AWS_SECRET_ACCESS_KEY:str

class Service:
    def __init__(self):
        config = Config()
        self.repository =  ShanyrakRepository(database)
        self.s3_service = S3Service(config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)
        self.here_service = HereService(config.HERE_API_KEY)

def get_service():
    return Service()
