from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, dictionary: dict) -> OnlineCourse:
        return cls(
            dictionary["name"],
            dictionary["description"],
            cls.days_to_weeks(dictionary["days"]))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)
