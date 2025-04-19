import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        total_of_weeks = math.ceil(days / 7)
        return total_of_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> None:
        for key, value in course_dict.items():
            cls.name = course_dict["name"]
            cls.description = course_dict["description"]
            cls.weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return cls
