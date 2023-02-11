from __future__ import annotations
from math import ceil


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.course_dict["name"] = name
        self.course_dict["description"] = description
        self.course_dict["weeks"] = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(course_dict["name"],
                   course_dict["description"],
                   cls.days_to_weeks(course_dict["days"]))
