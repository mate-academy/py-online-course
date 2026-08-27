from __future__ import annotations
from math import ceil


class OnlineCourse:
    # write your code here
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return int(ceil(days / 7))

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:

        instance = cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=0
        )

        if course_dict.get("days"):
            days = cls.days_to_weeks(course_dict["days"])
            instance.weeks = days
        else:
            instance.weeks = course_dict["weeks"]
        return instance

    def __str__(self) -> str:
        return self.description
