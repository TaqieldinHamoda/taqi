from typing import List
from pymongo import MongoClient
from server.models.database import Collection


class Pictures(Collection):
    """
    _id is name
    photo: base64 string

    TODO: Implement a route such that taqi.codestreet.app/pictures/name returns the base64 of the picture
    """
    def __init__(self, database: MongoClient) -> None:
        attributes = ["name", "photo", "description", "tags"]
        super().__init__(database=database, collection="Pictures", attributes=attributes)

        self.createIndex({"tags": 1})  # Multikey Index

    
    def getByName(self, name):
        return self.getByID(name)


    def getByTags(self, tags: List[str]):
        return self._get("tags", tags)
