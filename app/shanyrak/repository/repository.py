from typing import Any, Optional
from bson import ObjectId
from fastapi import Depends
from pymongo.database import Database

class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database
    def create_post_shanyraq(self, user_id: str,shan: dict[str, Any]) -> Optional[dict[str, Any]]:
        shan["user_id"] = ObjectId(user_id)
        sh = self.database["shanyraq"].insert_one(shan)
        return sh.inserted_id
    def get_shanyrak_by_id(self,  id : str) -> dict[str, Any]:
        return self.database["shanyraq"].find_one({"_id": ObjectId(id)})
    def update_shanyrak(self, id : str, inp : dict, jwt_id: str):
        filter = {"_id" : ObjectId(id), "user_id" : ObjectId(jwt_id)}
        update = {"$set" : {"type" : inp["type"], "price" : inp["price"],"address": inp["address"], "area" : inp["area"], "room_count": inp["rooms_count"], "description" : inp["description"]}}
        self.database["shanyraq"].update_one(filter, update)
    def delete_shanyrak(self, id : str, jwt_id : str):
        filter = {"_id" : ObjectId(id), "user_id": ObjectId(jwt_id)}
        self.database["shanyraq"].delete_one(filter)