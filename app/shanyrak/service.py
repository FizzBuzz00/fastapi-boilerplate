
from app.config import database
from .adapters.s3_service import S3Service

from .repository.repository import ShanyrakRepository



class Service:
    def __init__(
        self,
        repository: ShanyrakRepository,
        s3_service: S3Service
    ):
        self.repository = repository
        self.s3_service = s3_service

def get_service():
    repository = ShanyrakRepository(database)
    service  = S3Service()
    return Service(repository, service)
