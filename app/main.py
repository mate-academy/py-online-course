from __future__ import annotations
import math
from typing import Dict, Union


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(
            cls, course_dict: Dict[str, Union[str, int]]
    ) -> OnlineCourse:
        days = int(course_dict["days"])
        weeks = cls.days_to_weeks(days)

        return cls(
            name=str(course_dict["name"]),
            description=str(course_dict["description"]),
            weeks=weeks
        )
