from __future__ import annotations
import math


class OnlineCourse:

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        result = cls(name, description, weeks)
        return result

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
