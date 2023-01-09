import math
from typing import Any


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> Any:
        for key, value in course_dict.items():
            if "weeks" not in course_dict:
                if key == "days":
                    week_count = cls.days_to_weeks(value)
                    return cls(
                        name=course_dict.get("name"),
                        description=course_dict.get("description"),
                        weeks=week_count)
            else:
                return cls(
                    name=course_dict.get("name"),
                    description=course_dict.get("description"),
                    weeks=course_dict.get("weeks"))
