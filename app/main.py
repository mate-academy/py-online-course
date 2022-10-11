from math import ceil


class OnlineCourse:

    def __init__(self, name: str,
                 description: str,
                 weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = 7
        return ceil(days / week)

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        cls.course_dict = course_dict
        return cls(course_dict["name"],
                   course_dict["description"],
                   cls.days_to_weeks(course_dict["days"]))
