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
        course_day = course_dict["days"]
        course_week = cls.days_to_weeks(course_day)
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=course_week,
        )
