from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=OnlineCourse.days_to_weeks(course_dict["days"])
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        remaining_days = days % 7
        if remaining_days > 0:
            weeks += 1
        return weeks
