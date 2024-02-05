from __future__ import annotations

from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days_count: int) -> int:
        return ceil(days_count / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        weeks = cls.days_to_weeks(days_count=course_dict["days"])
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=weeks)
