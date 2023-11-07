import math


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        days = course_dict["days"]
        weeks = OnlineCourse.days_to_weeks(days)
        the_instance = cls(course_dict["name"],
                           course_dict["description"], weeks)
        return the_instance
