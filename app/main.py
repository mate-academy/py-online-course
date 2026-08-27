import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, days_dict: dict) -> "OnlineCourse":
        name = days_dict["name"]
        description = days_dict["description"]
        weeks = cls.days_to_weeks(days_dict["days"])
        return cls(name, description, weeks)
