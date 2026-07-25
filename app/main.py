from __future__ import annotations
import math


class OnlineCourse:
    # write your code here
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days <= 7:
            return 1
        quantity_of_weeks = days / 7
        if isinstance(quantity_of_weeks, float):
            return math.ceil(quantity_of_weeks)
        return quantity_of_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        converted_days_to_weeks = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"],
                   converted_days_to_weeks)
