from __future__ import annotations
import math


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
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, courses_dict: dict) -> OnlineCourse:
        return cls(
            courses_dict["name"],
            courses_dict["description"],
            cls.days_to_weeks(courses_dict["days"])
        )
