from typing import Any, Dict, List
from pymongo import database, ASCENDING
from models.database import Collection


class Pictures(Collection):
    """
    _id is name
    photo: base64 string

    TODO: Implement a route such that taqi.codestreet.app/pictures/name returns the base64 of the picture
    """
    def __init__(self, database: database.Database) -> None:
        attributes = ["name", "photo", "description", "tags"]
        super().__init__(database=database, collection="pictures", attributes=attributes)

        self.createIndex([('tags', ASCENDING)])  # Multikey Index

    
    def getByName(self, name) -> Dict[str, Any]:
        return self.getByID(name)


    def getByTags(self, tags: List[str]) -> List[Dict[str, Any]]:
        return self._get("tags", tags)
