from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"]),
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days / 7
        if weeks % 1 != 0:
            weeks += 1
        return math.floor(weeks)


dictionary = {
    "days": 13,
    "description": "The best course to start learning Python!",
    "name": "Python Basics",
}


python_course = OnlineCourse.from_dict(dictionary)
print(python_course.weeks)
