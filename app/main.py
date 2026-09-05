import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> object:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int | float:
        week = 7
        return math.ceil(days / week)

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        course = cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
        return course
