from __future__ import annotations
import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, input_dict: dict) -> OnlineCourse:
        return cls(input_dict["name"],
                   input_dict["description"],
                   OnlineCourse.days_to_weeks(input_dict["days"]))
