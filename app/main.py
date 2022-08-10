import math


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description

        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        return cls(
            name=course_dict['name'],
            description=course_dict['description'],
            weeks=OnlineCourse.days_to_weeks(course_dict['days']),
        )
