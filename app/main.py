import math


class OnlineCourse:
    def __init__(self,
                 name: str,
                 description: str,
                 weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
