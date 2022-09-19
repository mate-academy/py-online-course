from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        weeks = cls.days_to_weeks(course_dict["days"])
        name = course_dict["name"]
        description = course_dict["description"]
        return cls(name, description, weeks)


course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
# python_course = OnlineCourse.from_dict(course_dict)
# print(python_course.weeks)
