import math


class OnlineCourse:
    course_dict = {}

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        return cls(course_dict["name"], course_dict["description"],
                   OnlineCourse.days_to_weeks(course_dict["days"]))
