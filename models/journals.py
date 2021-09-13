from typing import Any, Dict, List
from pymongo import database, ASCENDING
from models.database import Collection


class Journals(Collection):
    """
    _id is title
    The photo_url belongs to the pictures class
    """
    def __init__(self, database: database.Database) -> None:
        attributes = ["title", "body", "photo_url", "description", "tags"]
        super().__init__(database=database, collection="journals", attributes=attributes)

        self.createIndex([('tags', ASCENDING)])  # Multikey Index

    
    def getByTitle(self, title) -> Dict[str, Any]:
        return self.getByID(title)


    def getByTags(self, tags: List[str]) -> List[Dict[str, Any]]:
        return self._get("tags", tags)
