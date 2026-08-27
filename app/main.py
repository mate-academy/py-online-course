from __future__ import annotations
from math import ceil


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> None:
        name = course_dict.get("name")
        description = course_dict.get("description")
        weeks = cls.days_to_weeks(course_dict.get("days"))
        return cls(name, description, weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)
