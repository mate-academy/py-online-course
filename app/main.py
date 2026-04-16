from __future__ import annotations
import math

class OnlineCourse:
    # write your code here
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course: dict) -> OnlineCourse:
        name = course["name"]
        description = course["description"]
        days = course["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
