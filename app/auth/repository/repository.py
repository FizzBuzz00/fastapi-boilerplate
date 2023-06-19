from datetime import datetime
from typing import Optional

from bson import ObjectId
from pymongo.database import Database

from ..utils.security import hash_password


class AuthRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_user(self, user: dict):
        payload = {
            "email": user["email"],
            "role":user["role"],
            "password": hash_password(user["password"]),
            "created_at": datetime.utcnow(),
        }

        self.database["users"].insert_one(payload)

    def get_user_by_id(self, user_id: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return user

    def get_user_by_email(self, email: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "email": email,
            }
        )
        return user
    
    def update_user_info(self, user_id: str, user: dict):
        filter = {"_id" : ObjectId(user_id)}
        update = {"$set" : user}
        user = self.database["users"].update_one(filter, update)
        
    def add_favorites_house(self, shanyraks:list):
        self.database["favorites"].insert_one(shanyraks)

    def get_only_address(self, house_id:str):
        val = self.database["shanyraq"].find_one({"_id": ObjectId(house_id)}, {"_id":1, "address":1})
        return val

    def get_favorites(self, user_id:str):
        val = self.database["favorites"].find({"user_id" : ObjectId(user_id)}, {"_id":0, "user_id":0})
        return list(val)
    
    def remove_favorites(self, fav_id:str, user_id:str):
        self.database["favorites"].delete_one({"_id":ObjectId(fav_id), "user_id": ObjectId(user_id)})