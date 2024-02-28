from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(
            self,
            name: str = None,
            description: str = None,
            weeks: int = None,
            course_dict: dict = None
    ) -> None:
        if course_dict:
            self.name = course_dict["name"]
            self.description = course_dict["description"]
            self.weeks = self.days_to_weeks(course_dict["days"])
        else:
            self.name = name
            self.description = description
            self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
