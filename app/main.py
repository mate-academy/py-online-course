from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(
            self,
            name: str,
            description: str,
            weeks: int
    ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        days = ceil(days / 7)
        return days

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name, description, weeks = (
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
        course = cls(name, description, weeks)
        return course
