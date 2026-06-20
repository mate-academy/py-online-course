from __future__ import annotations
from typing import TypedDict


class CourseDict(TypedDict):
    name: str
    description: str
    days: int


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days < 0:
            raise ValueError("days must be non-negative")

        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: CourseDict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"]),
        )
