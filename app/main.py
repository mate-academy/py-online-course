from __future__ import annotations
from math import ceil


class OnlineCourse:

    @staticmethod
    def days_to_weeks(day: int) -> int:
        return ceil(day / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:

        return OnlineCourse(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
