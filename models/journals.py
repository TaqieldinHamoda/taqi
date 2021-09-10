from typing import List
from pymongo import MongoClient
from server.models.database import Collection


class Journals(Collection):
    """
    _id is title
    The photo_url belongs to the pictures class
    """
    def __init__(self, database: MongoClient) -> None:
        attributes = ["title", "body", "photo_url", "description", "tags"]
        super().__init__(database=database, collection="Journals", attributes=attributes)

        self.createIndex({"tags": 1})  # Multikey Index

    
    def getByTitle(self, title):
        return self.getByID(title)


    def getByTags(self, tags: List[str]):
        return self._get("tags", tags)
