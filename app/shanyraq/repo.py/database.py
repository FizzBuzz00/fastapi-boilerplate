from winreg import HKEY_CURRENT_USER
from fastapi import Depends
from pymongo.database import Database

from app import shanyraq

class AuthRepository2:
    def __init__(self, database: Database):
        self.database = database
    def create_post_shanyraq(self, user_id: str = Depends(HKEY_CURRENT_USER)):
        shanyrak_dict = shanyraq.dict()
        shanyrak_dict["user_id"] = user_id
        shanyrak_id = self.database.shanyraks.insert_one(shanyrak_dict).inserted_id
        return {"_id": str(shanyrak_id)}
                             
