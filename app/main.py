import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        weeks = math.ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict):
        return cls(course_dict["name"], course_dict["description"],
                   cls.days_to_weeks(course_dict["days"]))
