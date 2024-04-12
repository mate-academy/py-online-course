from __future__ import annotations
import math


class OnlineCourse:
    curse_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, curse_dict: dict) -> OnlineCourse:
        return cls(
            curse_dict["name"],
            curse_dict["description"],
            cls.days_to_weeks(curse_dict["days"])
        )
