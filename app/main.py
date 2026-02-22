from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=course_dict["weeks"] if course_dict.get("weeks") is not None
            else cls.days_to_weeks(course_dict["days"])
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = ceil(days / 7)
        return weeks
