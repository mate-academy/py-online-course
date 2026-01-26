import math
from typing import Dict, Self


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: Dict) -> Self:
        name: str = course_dict.get("name", "")
        description: str = course_dict.get("description", "")
        days: int = course_dict.get("days", 0)
        weeks: int = cls.days_to_weeks(days)
        return cls(name, description, weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)
