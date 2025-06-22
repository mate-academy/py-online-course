from __future__ import annotations

import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)  # 7 day in the week

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        duration_in_days = cls.days_to_weeks(course_dict.get("days"))
        return cls(
            course_dict.get("name"),
            course_dict.get("description"),
            duration_in_days
        )
