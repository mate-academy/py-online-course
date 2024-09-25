from __future__ import annotations
import math


class OnlineCourse:
    course_dict = {}

    def __init__(self,
                 name: str,
                 description: str,
                 weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        weeks = cls.days_to_weeks(course_dict["days"])
        new_instance = cls(
            course_dict["name"],
            course_dict["description"],
            weeks
        )

        return new_instance
