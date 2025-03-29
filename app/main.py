from __future__ import annotations
import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = math.ceil(days / 7)
        return week

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        weeks = cls.days_to_weeks(course_dict["days"])
        n_course_dict = OnlineCourse(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
        return n_course_dict


course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)

print(course.description)  # The best course to start learn Python

print(OnlineCourse.days_to_weeks(10))  # == 2
print(OnlineCourse.days_to_weeks(14))  # == 2
print(OnlineCourse.days_to_weeks(15))  # == 3

course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}

python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # 2
