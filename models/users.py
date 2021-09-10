from typing import List
from pymongo import MongoClient
from models.database import Collection


class Likes(Collection):
    """
    _id is email
    photo_url: a url to the thing I like
    """
    def __init__(self, database: MongoClient) -> None:
        attributes = ["email", "name", "photo_url", "password_hash"]
        super().__init__(database=database, collection="Likes", attributes=attributes)

        self.createIndex({"tags": 1})  # Multikey Index

    
    def getByEmail(self, email):
        return self.getByID(email)

