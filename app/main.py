from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = 0
        if days % 7:
            weeks += 1
        weeks += days // 7
        return weeks

    @classmethod
    def from_dict(cls, course: dict) -> OnlineCourse:
        return cls(
            course["name"],
            course["description"],
            cls.days_to_weeks(course["days"])
        )
