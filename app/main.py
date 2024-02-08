from __future__ import annotations
from math import ceil


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_of_dict: dict) -> OnlineCourse:
        weeks = cls.days_to_weeks(course_of_dict["days"])
        print(weeks)
        return cls(
            name=course_of_dict["name"],
            description=course_of_dict["description"],
            weeks=weeks
        )
