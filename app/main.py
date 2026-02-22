import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> object:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> object:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        return cls(course_dict["name"], course_dict["description"],
                   cls.days_to_weeks(course_dict["days"]))
