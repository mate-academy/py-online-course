from __future__ import annotations
from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        convert this number to weeks.
        """

        week_days = 7
        return ceil(days / week_days)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        """
        convert this course_dict to an OnlineCourse instance.
        """
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])

        return cls(name=name, description=description, weeks=weeks)
