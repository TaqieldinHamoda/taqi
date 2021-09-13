from typing import Any, Dict, List, Union
from pymongo import MongoClient, database


class Collection:
    def __init__(self, database: database.Database, collection: str, attributes: List[str]) -> None:
        self._collection = database[collection]
        self._attributes = ["_id",] + attributes


    def _check(self, obj: dict) -> bool:
        try:
            for attribute in self._attributes:
                obj[attribute]

            return True
        except KeyError:
            return False


    def getAll(self) -> List[Dict[str, Any]]:
        return self._collection.find()


    def _get(self, index: str, key: Any) -> Dict[str, Any]:
        return self._collection.find({index: key})

    
    def getByID(self, ID: str) -> Dict[str, Any]:
        return self._get("_id", ID)


    def add(self, obj: dict) -> None:
        if not self._check(obj):
            raise Exception("Object is missing important attributes")

        self._collection.insert_one(obj)

    
    def addMany(self, objs: List[Dict]) -> None:
        for obj in objs:
            if not self._check(obj):
                raise Exception("Object is missing important attributes")

        self._collection.insert_many(objs)


    def createIndex(self, index: Union[str, Dict[str, int]]) -> None:
        self._collection.create_index(index)


class Database:
    def __init__(self, user: str, password: str, cluster: str) -> None:
        CONNECTION_STRING = f"mongodb+srv://{user}:{password}@{cluster}.mongodb.net/personalWebsite?retryWrites=true&w=majority"
        self._database = MongoClient(CONNECTION_STRING)

    
    def getDatabase(self, database: str) -> database.Database:
        return self._database[database]
    
