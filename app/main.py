import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course: dict):
        return cls(
            course["name"],
            course["description"],
            OnlineCourse.days_to_weeks(course["days"])
        )
