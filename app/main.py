from __future__ import annotations
import math


class OnlineClass:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineClass:
        course = cls("", "", 0)
        course.name = course_dict.get("name")
        course.description = course_dict.get("description")
        course.weeks = cls.days_to_weeks(course_dict.get("days"))
        return course
