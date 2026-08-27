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
    def from_dict(cls, dict_c: dict) -> OnlineCourse:
        weeks = math.ceil((dict_c["days"]) / 7)
        dict_c = cls(dict_c["name"], dict_c["description"], weeks)
        return dict_c
