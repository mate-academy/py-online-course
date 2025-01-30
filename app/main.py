from __future__ import annotations
from math import ceil
from typing import Dict


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: Dict[str, str | int]) -> OnlineCourse:
        name = course_dict.get("name")
        description = course_dict.get("description")
        days = course_dict.get("days")
        return cls(name=name, description=description, weeks=cls.days_to_weeks(days))


course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)
print(course.description)  # The best course to start learn Python

print(


    OnlineCourse.days_to_weeks(10),  # 2
    OnlineCourse.days_to_weeks(14),  # 2
    OnlineCourse.days_to_weeks(15)  # 3
)


course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # 2
