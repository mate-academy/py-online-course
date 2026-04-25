from __future__ import annotations
import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return int(math.ceil(days / 7))

    @classmethod
    def from_dict(cls, cource_dict: dict) -> OnlineCourse:
        return cls(
            name=cource_dict.get("name"),
            description=cource_dict.get("description"),
            weeks=cls.days_to_weeks(cource_dict.get("days")),
        )
