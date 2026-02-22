from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    def course_dict(self) -> dict:
        return {"name": self.name,
                "description": self.description, "weeks": self.weeks}

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> str | OnlineCourse:
        print(f"course_dict: {course_dict}")

        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)

        return cls(name=name, description=description, weeks=weeks)
