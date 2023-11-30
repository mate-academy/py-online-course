import math


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict):
        return cls(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(course_dict["days"])
        )

    @staticmethod
    def days_to_weeks(days):
        weeks = math.ceil(days / 7)
        return weeks
