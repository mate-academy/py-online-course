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
        name, description, weeks = (
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"]),
        )
        return cls(name, description, weeks)
