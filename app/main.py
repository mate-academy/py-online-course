import math


class OnlineCourse:

    @staticmethod
    def days_to_weeks(days: int) -> int:

        days_to_weeks = math.ceil(days / 7)
        return days_to_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":

        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        return cls(name, description, cls.days_to_weeks(days))

    def __init__(self, name: str, description: str, weeks: int) -> None:

        self.name = name
        self.description = description
        self.weeks = weeks
