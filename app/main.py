from __future__ import annotations

import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        day_in_week = 7
        return math.ceil(days / day_in_week)

    @classmethod
    def from_dict(cls, course_dict: dict[str]) -> OnlineCourse:
        return cls(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(course_dict["days"])
        )
