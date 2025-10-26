import math
from typing import Dict, Any


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days <= 0:
            return 0
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: Dict[str, Any]) -> "OnlineCourse":
        name: str = course_dict["name"]
        description: str = course_dict["description"]
        days: int = course_dict["days"]
        weeks: int = cls.days_to_weeks(days)
        return cls(name=name, description=description, weeks=weeks)
