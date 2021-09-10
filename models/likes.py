from typing import List
from pymongo import MongoClient
from server.models.database import Collection


class Likes(Collection):
    """
    _id is name
    photo_url: a url to the thing I like
    """
    def __init__(self, database: MongoClient) -> None:
        attributes = ["name", "photo_url", "description", "tags"]
        super().__init__(database=database, collection="Likes", attributes=attributes)

        self.createIndex({"tags": 1})  # Multikey Index

    
    def getByName(self, name):
        return self.getByID(name)


    def getByTags(self, tags: List[str]):
        return self._get("tags", tags)
