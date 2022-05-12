import math


class OnlineCourse:

    @staticmethod
    def days_to_weeks(days):
        if days % 7 == 0:
            return math.floor((days / 7))
        return math.floor((days / 7)) + 1

    @classmethod
    def from_dict(cls, course_dict):
        return OnlineCourse(course_dict["name"],
                            course_dict["description"],
                            OnlineCourse.days_to_weeks(course_dict["days"])
                            )

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks
