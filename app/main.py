import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name: str = name
        self.description: str = description
        self.weeks: int = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        days = course_dict.get("days", 0)
        weeks = cls.days_to_weeks(days)
        return cls(course_dict["name"], course_dict["description"], weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)
