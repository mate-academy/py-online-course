class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = OnlineCourse.days_to_weeks(days)
        return cls(name, description, weeks)


course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)
print(course.description)

course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)

course_dict = {
    "name": "Advanced Python",
    "description": "Become a Python Guru",
    "days": 15,
}

advanced_python_course = OnlineCourse.from_dict(course_dict)
print(advanced_python_course.weeks)

course_dict = {
    "name": "Data Science with Python",
    "description": "Learn how to analyze data with Python",
    "days": 21,
}
data_science_course = OnlineCourse.from_dict(course_dict)
print(data_science_course.weeks)
