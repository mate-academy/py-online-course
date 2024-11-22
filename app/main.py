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
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        week = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"],
                            course_dict["description"],
                            week)

# course_dict = {
#     "name": "Python Core",
#     "description": "After this course you will know everything about Python",
#     "days": 12,
# }
# python_course = OnlineCourse.from_dict(course_dict)
# print(python_course.weeks)
