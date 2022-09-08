import math


class OnlineCourse:
    course_dict = []

    def __init__(self, name: str, description: str, weeks: int):
        self.course_dict.append(self)
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days % 7 != 0:
            return math.floor((days / 7) + 1)
        return math.floor(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=OnlineCourse.days_to_weeks(days=course_dict["days"])
        )
