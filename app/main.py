from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(
            self, name: str, description: str, weeks: int, **kwargs
    ) -> None:
        self.name, self.description, self.weeks = name, description, weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(weeks=cls.days_to_weeks(course_dict["days"]), **course_dict)
