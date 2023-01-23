import math

class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict) -> None:
        return cls(course_dict["name"], course_dict["description"], cls.days_to_weeks(course_dict["days"]))


    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = 0
        if days > 0 and days <= 7:
            weeks = 1
        else:
            weeks = math.ceil(days / 7)
        return weeks