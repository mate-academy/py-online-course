import math


class OnlineCourse:
    course = []

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.course.append(self)

    def course_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "weeks": self.weeks
        }

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, data: dict) -> "OnlineCourse":
        weeks = cls.days_to_weeks(data["days"])
        return cls(data["name"], data["description"], weeks)

    def __repr__(self) -> str:
        return (
            f"OnlineCourse({self.name}, "
            f"{self.description}, "
            f"{self.weeks} weeks)"
        )
