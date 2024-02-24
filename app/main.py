import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> any:
        name_course = course_dict["name"]
        description_course = course_dict["description"]
        days_course = course_dict["days"]
        return cls(name=name_course, description=description_course,
                   weeks=cls.days_to_weeks(days_course))
