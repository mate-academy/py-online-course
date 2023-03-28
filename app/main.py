class OnlineCourse:
    # write your code here
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = int(days / 7)
        remainder = days % 7
        if remainder:
            weeks = weeks + 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict):
        course = cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"]),
        )
        return course


if __name__ == "__main__":
    course = OnlineCourse(
        name="Python Basics",
        description="The best course to start learning Python",
        weeks=2,
    )
    print(course.description)

    print(OnlineCourse.days_to_weeks(10) == 2)
    print(OnlineCourse.days_to_weeks(14) == 2)
    print(OnlineCourse.days_to_weeks(15) == 3)

    course_dict = {
        "name": "Python Core",
        "description": "After this course you will know everything about Python",
        "days": 12,
    }

    python_course = OnlineCourse.from_dict(course_dict)
    print(python_course.description)
