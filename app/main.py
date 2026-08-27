import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days <= 0:
            return 0
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        course_name = course_dict["name"]
        course_description = course_dict["description"]
        course_days = course_dict["days"]

        course_weeks = cls.days_to_weeks(course_days)

        return cls(
            name=course_name,
            description=course_description,
            weeks=course_weeks
        )
