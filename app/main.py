from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, **kwargs) -> None:
        self.name = name
        self.description = description
        if "weeks" in kwargs:
            self.weeks = kwargs["weeks"]
        else:
            self.weeks = self.days_to_weeks(kwargs["days"])

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(course_dict["name"],course_dict["description"],
                   days=course_dict["days"])
