from __future__ import annotations

import math
from typing import Any

ImmutableKey = int | str


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict[ImmutableKey, Any]) -> OnlineCourse:
        return cls(
            name=course_dict.get("name", "Untitled"),
            description=course_dict.get("description", ""),
            weeks=cls.days_to_weeks(course_dict.get("days", 0))
        )

    @staticmethod
    def days_to_weeks(day: int) -> int:
        if not isinstance(day, int):
            return 0
        return int(math.ceil(day / 7))
