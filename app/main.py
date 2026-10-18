from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days // 7 + (days % 7 != 0)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name, description, days = course_dict.values()
        return cls(name, description, cls.days_to_weeks(days))
