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
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        course_dict["name"] = course_dict.get("name", "")
        course_dict["description"] = course_dict.get("description", "")
        course_dict["days"] = course_dict.get("days", "")
        course_dict["weeks"] = cls.days_to_weeks(course_dict["days"])
        return cls(
            course_dict["name"],
            course_dict["description"],
            course_dict["weeks"]
        )
