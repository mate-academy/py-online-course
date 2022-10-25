import math
from typing import Callable


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> Callable:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        res = math.ceil(days / 7)
        return res

    @classmethod
    def from_dict(cls, course_dict: dict) -> Callable:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
