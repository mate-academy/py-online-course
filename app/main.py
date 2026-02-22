from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(
            self,
            name: str,
            description: str,
            weeks: int
    ) -> OnlineCourse:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, cours_dict: dict) -> OnlineCourse:
        return cls(
            cours_dict["name"],
            cours_dict["description"],
            cls.days_to_weeks(cours_dict["days"])
        )
