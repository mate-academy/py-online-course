from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = 1
        for day in range(7, days, 7):
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        days = course_dict["days"]
        weeks_final = cls.days_to_weeks(days)
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks_final,
        )
