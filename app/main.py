import math


class OnlineCourse:
    course_dictionary = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = 7
        return math.ceil(days / week)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        course_instance = cls(course_dict["name"],
                              course_dict["description"],
                              cls.days_to_weeks(course_dict["days"]))
        return course_instance
