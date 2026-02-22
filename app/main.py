import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def days_to_weeks(cls, days):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        cls.name = course_dict["name"]
        cls.description = course_dict["description"]
        cls.weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return cls
