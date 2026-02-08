class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days // 7 + (1 if days % 7 > 0 else 0))

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return OnlineCourse(course_dict["name"], course_dict["description"], weeks)


course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}


python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # 2