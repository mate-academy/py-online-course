from __future__ import annotations
from math import ceil


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int | float:
        week = days / 7
        return ceil(week)

    @classmethod
    def from_dict(cls, course_dict) -> OnlineCourse:
        return cls(
            course_dict.get("name"),
            course_dict.get("description"),
            OnlineCourse.days_to_weeks(course_dict.get("days"))
        )


