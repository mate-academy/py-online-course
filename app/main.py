from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(
            self,
            name: str,
            description: str,
            weeks: int,
            *args, **kwargs
    ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(day: int) -> int:
        return ceil(day / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        course_dict["weeks"] = cls.days_to_weeks(course_dict["days"])
        return cls(**course_dict)
