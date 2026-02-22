import math


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        if "days" in course_dict:
            weeks = cls.days_to_weeks(course_dict["days"])
            course_dict.pop("days")
            course_dict["weeks"] = weeks

        return cls(
            course_dict["name"],
            course_dict["description"],
            course_dict["weeks"]
        )
