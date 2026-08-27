from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """one week = 7 days"""
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        week = cls.days_to_weeks(days)
        return cls(name, description, week)


def create_course(course_dict: dict) -> OnlineCourse:
    return OnlineCourse.from_dict(course_dict)
