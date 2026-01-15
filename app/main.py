import math


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.days = None
        OnlineCourse.course_dict[self.name] = self
        OnlineCourse.course_dict[self.description] = self
        OnlineCourse.course_dict[self.days] = self.weeks * 7

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        if "days" in course_dict:
            weeks = OnlineCourse.days_to_weeks(course_dict["days"])
            course_dict["weeks"] = weeks
            del course_dict["days"]
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=course_dict["weeks"])
