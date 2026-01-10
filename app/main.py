from __future__ import annotations

from typing import Any


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days - 1) // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict[str, Any]) -> OnlineCourse:
        cls.name = course_dict["name"]
        cls.description = course_dict["description"]
        cls.weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name=cls.name, description=cls.description, weeks=cls.weeks)
