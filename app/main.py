from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: str) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int | float:
        count = 0
        special_variable = 0
        while days > special_variable:
            special_variable += 7
            count += 1
        return count

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
