from typing import Any, Optional
from bson import ObjectId
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
        update = {"$set" : inp}
        self.database["shanyraq"].update_one(filter, update)

    def delete_shanyrak(self, id : str, jwt_id : str):
        filter = {"_id" : ObjectId(id), "user_id": ObjectId(jwt_id)}
        self.database["shanyraq"].delete_one(filter)

    def add_image_shanyrak(self, house_id : str, media : list):
        filter = {"_id" : ObjectId(house_id)}
        update = {"$push" : {"media" : media}}
        self.database["shanyraq"].update_one(filter, update)

    def delete_media(self, house_id:str):
        filter = {"_id":ObjectId(house_id)}
        update = {"$unset":{"media": 1}}
        self.database["shanyraq"].update_one(filter, update)
        
    def show_option(self, house_id:str) -> dict[str, list]:
        return self.database["shanyraq"].find_one({"_id": ObjectId(house_id)}, {"_id": 0, "media":1})
    
    def upload_avatar(self, user_id, image : str):
        filter = {"_id" : ObjectId(user_id)}
        up = {"$set" : {"avatar_url" : image}}
        self.database["users"].update_one(filter, up)
    
    def delete_avatar(self, user_id : str):
        self.database["users"].update_one({"_id":ObjectId(user_id)}, {"$unset" : {"avatar_url" : 1}})
    
    def return_ava(self, user_id):
        return self.database["users"].find_one({"_id": ObjectId(user_id)}, {"avatar_url" : 1})