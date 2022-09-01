import math


class OnlineCourse:

    course_dict = {}

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks
        self.__class__.course_dict = {
            "name": self.name,
            "description": self.description,
            "weeks": self.weeks
        }

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        cls.course_dict = course_dict
        return cls(
            cls.course_dict["name"],
            cls.course_dict["description"],
            cls.days_to_weeks(cls.course_dict["days"])
        )
