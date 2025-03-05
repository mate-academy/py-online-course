import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> str:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> object:
        weeks = math.ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict: list) -> object:
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)