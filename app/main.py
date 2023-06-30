import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        weeks = math.ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict):
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(
            course_dict["name"],
            course_dict["description"],
            weeks
        )
