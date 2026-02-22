from __future__ import annotations
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
    def from_dict(cls, course_dic: dict) -> OnlineCourse:
        name = course_dic["name"]
        description = course_dic["description"]
        days = course_dic["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
