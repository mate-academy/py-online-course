from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course: dict) -> "OnlineCourse":
        days = course["days"]
        weeks = cls.days_to_weeks(days)
        return cls(course["name"], course["description"], weeks)
