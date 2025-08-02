import math

class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
    @staticmethod
    def days_to_week(days: int) -> int:
        return math.ceil(days / 7)
    def from_dict(cls, course_dict: dict):
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = OnlineCourse.days_to_week(days)
        return cls(name, description, weeks)
