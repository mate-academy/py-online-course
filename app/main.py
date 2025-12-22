from __future__ import annotations
import math


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = 7    # 7 days a week
        return math.ceil(days / week)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        course_dict["weeks"] = cls.days_to_weeks(course_dict["days"])
        return cls.__call__(
            course_dict["name"],
            course_dict["description"],
            course_dict["weeks"]
        )
