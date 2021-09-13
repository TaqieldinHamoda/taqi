from typing import Any, Dict, List
from pymongo import database, ASCENDING
from models.database import Collection


class Likes(Collection):
    """
    _id is name
    photo_url: a url to the thing I like
    """
    def __init__(self, database: database.Database) -> None:
        attributes = ["name", "photo_url", "description", "tags"]
        super().__init__(database=database, collection="likes", attributes=attributes)

        self.createIndex([('tags', ASCENDING)])  # Multikey Index

    
    def getByName(self, name) -> Dict[str, Any]:
        return self.getByID(name)


    def getByTags(self, tags: List[str]) -> List[Dict[str, Any]]:
        return self._get("tags", tags)
