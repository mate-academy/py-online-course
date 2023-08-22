import math
from typing import Callable


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int | float:
        result = math.ceil(days / 7)
        return result

    @classmethod
    def from_dict(cls, course_dict: dict):
        name = course_dict.get("name")
        description = course_dict.get("description")
        days = cls.days_to_weeks(course_dict.get("days"))

        return cls(name, description, days)
