import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

course_dict = {
    "name": "Advanced Python",
    "description": "Deep dive into decorators and generators",
    "days": 10
}

weeks_needed = OnlineCourse.days_to_weeks(course_dict["days"])

new_course = OnlineCourse(
    name=course_dict["name"],
    description=course_dict["description"],
    weeks=weeks_needed
)
print(f"Kurs: {new_course.name} trwa {new_course.weeks} tyg.")
