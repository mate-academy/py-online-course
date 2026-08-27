import math
from typing import Any


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.__class__.__name__ = "OnlineClass"

    @staticmethod
    def days_to_weeks(days: int) -> int:
        num_of_weeks = days / 7
        return math.ceil(num_of_weeks)

    @classmethod
    def from_dict(cls, course_dict: dict) -> Any:
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        instance_course = OnlineCourse(name, description, weeks)
        return instance_course
