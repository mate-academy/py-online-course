from __future__ import annotations

import math
from typing import TypedDict


class CourseDict(TypedDict):
    name: str
    description: str
    days: int


class OnlineCourse:
    DAYS_IN_WEEK = 7

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return int(math.ceil(days / OnlineCourse.DAYS_IN_WEEK))

    @classmethod
    def from_dict(cls, course_dict: TypedDict) -> OnlineCourse:
        return cls(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(course_dict["days"]),
        )
