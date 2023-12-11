from __future__ import annotations
import math


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        days = course_dict["days"]
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
