import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """Creates an OnlineCourse instance from a dictionary with keys:
        "name", "description", and "days"."""
        name = course_dict.get("name")
        description = course_dict.get("description")
        days = course_dict.get("days")
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """Converts days to weeks, rounded to 1 decimal"""
        return math.ceil(days / 7)
