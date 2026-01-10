import math


class OnlineCourse:

    courses = []

    def __init__(self, name: str, description: str,
                 weeks: int | float) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.courses.append(self)

    @staticmethod
    def days_to_weeks(days: int) -> float:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        weeks = cls.days_to_weeks(course_dict["days"])
        course = cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
        return course
