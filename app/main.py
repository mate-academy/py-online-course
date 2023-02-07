from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self,
                 name: str,
                 description: str,
                 weeks: float | int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> float:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name = course_dict.get("name")
        description = course_dict.get("description")
        weeks = cls.days_to_weeks(course_dict.get("days"))

        return cls(name=name, description=description, weeks=weeks)
