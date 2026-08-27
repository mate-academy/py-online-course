from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, some_course_dict: dict) -> OnlineCourse:
        return cls(some_course_dict["name"], some_course_dict["description"],
                   cls.days_to_weeks(some_course_dict["days"]))
