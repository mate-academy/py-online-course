from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        lenght_of_week = 7
        duration_in_weeks = math.ceil(days / lenght_of_week)

        return duration_in_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        cls.__name__ = "OnlineClass"
        course_duration_in_days = course_dict["days"]
        return OnlineCourse(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_duration_in_days),
        )
