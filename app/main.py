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
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)


# Example usage
course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)
print(course.description)  # Output: The best course to start learning Python

course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # Output: 2
