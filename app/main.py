from math import ceil
from typing import Self


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.course_dict: dict = {
            "name": self.name,
            "description": self.description,
            "weeks": self.weeks
        }

    @staticmethod
    def days_to_weeks(number_of_days: int) -> int:
        return ceil(number_of_days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> Self:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
