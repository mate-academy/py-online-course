import math


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    def __str__(self):
        return f"{self.name} - {self.description}"

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7)


    @classmethod
    def from_dict(cls, course_dict):
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"]),
        )
