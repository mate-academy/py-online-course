import math


class OnlineCourse:
    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dic: dict) -> "OnlineCourse":
        return cls(
            name=course_dic["name"],
            description=course_dic["description"],
            weeks=cls.days_to_weeks(course_dic["days"])
        )

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks


course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}

python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # 2
