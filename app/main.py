from __future__ import annotations
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return OnlineCourse(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=OnlineCourse.days_to_weeks(course_dict["days"])
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)


course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
python_course = OnlineCourse.from_dict(course_dict)

print(python_course.weeks)  # 2

print(type(python_course))
