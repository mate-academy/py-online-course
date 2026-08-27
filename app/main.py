from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days / 7
        return math.ceil(weeks)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        name = course_dict["name"]
        description = course_dict["description"]
        return cls(name, description, weeks)
