from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(num: int) -> int:
        return (num + 6) // 7

    @classmethod
    def from_dict(cls, course: dict) -> OnlineCourse:
        days = cls.days_to_weeks(course["days"])
        return cls(course["name"], course["description"], days)
