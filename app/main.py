from __future__ import annotations


class OnlineCourse:
    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days / 7
        if weeks % 1:
            weeks = days // 7 + 1

        return weeks

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
