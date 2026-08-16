from __future__ import annotations
import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        number_of_weeks = math.ceil(days / 7)
        return number_of_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        course_data = {}
        for key, value in course_dict.items():
            if key == "days":
                course_data["weeks"] = cls.days_to_weeks(value)
            elif key == "name":
                course_data["name"] = value
            elif key == "description":
                course_data["description"] = value
        return cls(**course_data)
