from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse | ValueError:
        if course_dict.get("name") and course_dict.get("description") and course_dict.get("days"):
            return cls(course_dict["name"], course_dict["description"], cls.days_to_weeks(course_dict["days"]))
        elif course_dict.get("name") and course_dict.get("description") and course_dict.get("weeks"):
            return cls(course_dict["name"], course_dict["description"], course_dict["weeks"])
        return ValueError("Invalid course dict")

    @staticmethod
    def days_to_weeks(days: int) -> int | None:
        days_in_week = 7
        if days > 0 and isinstance(days, int):
            return math.ceil(days / days_in_week)
        return None



