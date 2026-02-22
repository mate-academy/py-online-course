from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        days_from_dict = course_dict["days"]
        week = OnlineCourse.days_to_weeks(days_from_dict)
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=week
        )
