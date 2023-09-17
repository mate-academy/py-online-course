from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name = course_dict.get("name")
        description = course_dict.get("description")
        days = course_dict.get("days")

        if days:
            weeks = cls.days_to_weeks(days)
        else:
            weeks = 0

        return cls(name, description, weeks)
