from __future__ import annotations
from math import ceil


class OnlineCourse:

    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        if kwargs.get("days") is not None:
            self.weeks = OnlineCourse.days_to_weeks(kwargs.get("days"))
        elif kwargs.get("weeks") is not None:
            self.weeks = kwargs.get("weeks")

    @staticmethod
    def days_to_weeks(days: int) -> float:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(name=course_dict.get("name"),
                   description=course_dict.get("description"),
                   days=course_dict.get("days"))
