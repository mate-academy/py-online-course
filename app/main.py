import math


class OnlineCourse:
    def __init__(self, name, description, weeks) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(weeks):
        return math.ceil(weeks / 7)

    @classmethod
    def from_dict(cls, course_dict):
        cls.name = course_dict["name"]
        cls.description = course_dict["description"]
        cls.weeks = cls.days_to_weeks(course_dict["days"])
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"]),
        )
