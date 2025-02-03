from __future__ import annotations
import math


class OnlineCourse:
    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7.0)
    pass

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course: dict) -> OnlineCourse:
        return cls(course["name"],
                   course["description"],
                   cls.days_to_weeks(course["days"]))
