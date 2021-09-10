from pymongo import MongoClient
from server.models.database import Collection


class GoalType:
    MONTH = 0
    ANNUAL = 1
    DECADE = 2
    MAX = 2


class GoalDifficulty:
    EASY = 0
    INTERMEDIATE = 1
    HARD = 2
    EXTREME = 3
    MAX = 3


class GoalGroup:
    COMPLETED = 0
    MONTHLY = 1
    NY_RESOLUTION = 2
    THIRTY_BEFORE_THIRTY = 3
    MAX = 3


class Goals(Collection):
    """
    _id is name
    """
    def __init__(self, database: MongoClient) -> None:
        attributes = ["type", "difficulty", "name", "description", "group"]
        super().__init__(database=database, collection="Goals", attributes=attributes)

        self.createIndex("type")
        self.createIndex("difficulty")
        self.createIndex("group")

    
    def _check(self, obj: dict):
        try:
            for attribute in self._attributes:
                if attribute == "type":
                    if (obj[attribute] < 0) or (obj[attribute] > GoalType.MAX):
                        raise Exception("Unknown goal type")
                elif attribute == "difficulty":
                    if (obj[attribute] < 0) or (obj[attribute] > GoalDifficulty.MAX):
                        raise Exception("Unknown goal difficulty")
                elif attribute == "group":
                    if (obj[attribute] < 0) or (obj[attribute] > GoalGroup.MAX):
                        raise Exception("Unknown goal group")
                else:
                    obj[attribute]

            return True
        except KeyError:
            return False


    def getByName(self, name):
        self.getByID(name)

    
    def getByType(self, goal_type: int):
        if (goal_type < 0) or (goal_type > GoalType.MAX):
            raise Exception("Unknown goal type")

        return self._get("type", goal_type)


    def getByDifficulty(self, difficulty: int):
        if (difficulty < 0) or (difficulty > GoalDifficulty.MAX):
            raise Exception("Unknown goal difficulty")

        return self._get("difficulty", difficulty)


    def getByGroup(self, group: int):
        if (group < 0) or (group > GoalGroup.MAX):
            raise Exception("Unknown goal group")

        return self._get("group", group)


    def getByCompleted(self):
        return self._get("group", GoalGroup.COMPLETED)