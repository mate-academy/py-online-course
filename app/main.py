from __future__ import annotations
import math


class OnlineCourse:
    course_dict = {}

    def __init__(
            self, name: str,
            description: str,
            weeks: int | float
    ) -> None:
        self. name = name
        self.description = description
        self. weeks = weeks

    @staticmethod
    def days_to_weeks(days: int | float) -> int:
        return (math.ceil(days / 7))

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        cls.course_dict = course_dict

        if "days" in course_dict:
            days = course_dict.get("days")
            weeks = cls.days_to_weeks(days)
            course_dict["weeks"] = weeks
            del course_dict["days"]

        return cls(
            name=course_dict.get("name"),
            description=course_dict.get("description"),
            weeks=course_dict.get("weeks")
        )
