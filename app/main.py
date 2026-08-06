from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        return cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )


course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)
print(course.weeks)
print(OnlineCourse.days_to_weeks(15))
course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}

python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # 2
