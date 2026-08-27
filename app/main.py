from __future__ import annotations
import math


class OnlineCourse:

    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.course_dict["name"] = name
        OnlineCourse.course_dict["description"] = description
        OnlineCourse.course_dict["weeks"] = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        print(f"Days {days} to week is: {math.ceil(days / 7)}")
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=OnlineCourse.days_to_weeks(course_dict["days"])
        )


course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)
print(course.description)

course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # 2
print(python_course.name)
print(python_course.description)
