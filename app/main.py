from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(self, name: str,
                 description: str,
                 weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days <= 0:
            return 0
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dct: dict) -> OnlineCourse:
        weeks = cls.days_to_weeks(course_dct["days"])
        return cls(name=course_dct["name"],
                   description=course_dct["description"],
                   weeks=weeks)
