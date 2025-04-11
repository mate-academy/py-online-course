from __future__ import annotations
import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        result = math.ceil(days / 7)
        return result

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:

        course_dict["weeks"] = math.ceil(course_dict["days"] / 7)
        new_inst = cls(
            course_dict["name"],
            course_dict["description"],
            course_dict["weeks"]
        )
        return new_inst
