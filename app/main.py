import math


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

        OnlineCourse.course_dict["name"] = self.name
        OnlineCourse.course_dict["description"] = self.description
        OnlineCourse.course_dict["weeks"] = self.weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> any:
        return cls(
            course_dict.get("name"), course_dict.get("description"),
            cls.days_to_weeks(course_dict.get("days"))
        )
