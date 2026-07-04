from __future__ import annotations
import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        result = math.ceil(days / 7)
        return result

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=OnlineCourse.days_to_weeks(course_dict["days"])
                   )
