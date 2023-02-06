from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = 7
        weeks = 1
        while week < days:
            weeks += 1
            week += 7
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        values = [*course_dict.values()]
        new = object.__new__(cls)
        new.name, new.description, new.weeks = (
            values[0],
            values[1],
            cls.days_to_weeks(values[2]),
        )
        return new
