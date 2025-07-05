import math


class OnlineCourse:
    def __init__(self,
                 name: str,
                 description: str,
                 weeks: int
                 ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course: dict) -> "OnlineCourse":
        weeks = cls.days_to_weeks(course["days"])
        return cls(course["name"], course["description"], weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)
