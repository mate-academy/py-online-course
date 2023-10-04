from __future__ import annotations
from math import ceil

class OnlineCourse:

    def __init__(self, name, description, weeks) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        number_of_weeks = ceil(days / 7)
        return number_of_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:

        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])

        online_course = cls(name, description, weeks)

        return online_course

