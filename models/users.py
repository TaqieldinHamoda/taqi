from typing import Any, Dict
from pymongo import database
from models.database import Collection


class Users(Collection):
    """
    _id is email
    photo_url: a url to the thing I like
    """
    def __init__(self, database: database.Database) -> None:
        attributes = ["email", "name", "photo_url", "password_hash"]
        super().__init__(database=database, collection="users", attributes=attributes)

        self.createIndex({"tags": 1})  # Multikey Index

    
    def getByEmail(self, email) -> Dict[str, Any]:
        return self.getByID(email)

