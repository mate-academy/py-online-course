import math


class OnlineCourse:

    def __init__(self,
                 name: str,
                 description: str,
                 weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        one_week = 7
        return math.ceil(days / one_week)

    @classmethod
    def from_dict(cls, course_dict: dict):
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(
            course_dict["name"],
            course_dict["description"],
            weeks
        )
