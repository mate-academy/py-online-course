import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days <= 0:
            raise ValueError("course days cannot be negative")
        weeks = days / 7
        return math.ceil(weeks)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        if not course_dict:
            raise ValueError("course_dict cannot be empty")
        if not course_dict.get("name"):
            raise ValueError("course name cannot be empty")
        if not course_dict.get("description"):
            raise ValueError("course description cannot be empty")
        if not course_dict.get("days"):
            raise ValueError("course days cannot be empty")

        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name, description, weeks)

    def __str__(self) -> str:
        return f"{self.name}\n{self.description}\n{self.weeks} weeks"
