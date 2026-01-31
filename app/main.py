import math


class OnlineCourse:
    course_dict = {}

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.course_dict["name"] = name
        OnlineCourse.course_dict["description"] = description
        OnlineCourse.course_dict["days"] = weeks * 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        new_course = cls(course_dict["name"], course_dict["description"],
                         OnlineCourse.days_to_weeks(course_dict["days"]))
        return new_course
