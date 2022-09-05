import math


class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        weeks = math.ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict):
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        course = cls(name, description, weeks)
        return course
