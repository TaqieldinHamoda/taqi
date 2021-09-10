from typing import Any, Dict, List
from pymongo import MongoClient


class Collection:
    def __init__(self, database: MongoClient, collection: str, attributes: List[str]) -> None:
        self._collection = database[collection]
        self._attributes = ["_id",] + attributes


    def _check(self, obj: dict):
        try:
            for attribute in self._attributes:
                obj[attribute]

            return True
        except KeyError:
            return False


    def getAll(self):
        return self._collection.find()


    def _get(self, index: str, key: Any):
        return self._collection.find({index: key})

    
    def getByID(self, ID: str):
        return self._get("_id", ID)


    def add(self, obj: dict):
        if not self._check(obj):
            raise Exception("Object is missing important attributes")

        self._collection.insert_one(obj)

    
    def addMany(self, objs: List[Dict]):
        for obj in objs:
            if not self._check(obj):
                raise Exception("Object is missing important attributes")

        self._collection.insert_many(objs)


    def createIndex(self, index):
        self._collection.create_index(index)


class Database:
    def __init__(self, user, password, cluster, database) -> None:
        CONNECTION_STRING = f"mongodb+srv://{user}:{password}@{cluster}.mongodb.net/personalWebsite?retryWrites=true&w=majority"
        self._database = MongoClient(CONNECTION_STRING)[database]

    
    def getDatabase(self):
        return self._client


    
