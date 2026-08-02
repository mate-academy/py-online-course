import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = math.ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        name = course_dict.get("name")
        descr = course_dict.get("description")
        days = course_dict.get("days")
        weeks = cls.days_to_weeks(days=days)
        return cls(name=name, description=descr, weeks=weeks)
