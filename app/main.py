from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    def __str__(self) -> str:
        return self.description

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7  # Або import math -> return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, data: dict) -> OnlineCourse:
        return cls(
            data["name"], data["description"], cls.days_to_weeks(data["days"])
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
print(python_course.weeks)
