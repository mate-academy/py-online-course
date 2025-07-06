import math
from typing import Self


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> Self:
        weeks = cls.days_to_weeks(course_dict.get("days"))
        description = course_dict.get("description")
        name = course_dict.get("name")
        return cls(name, description, weeks)
