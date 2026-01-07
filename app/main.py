from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, data: dict) -> OnlineCourse:
        return cls(
            name=data["name"],
            description=data["description"],
            weeks=cls.days_to_weeks(data["days"])
        )
