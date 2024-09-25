from __future__ import annotations


class OnlineCourse:
    def __init__(
            self,
            name: str,
            description: str,
            weeks: int | float
    ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = 0
        for i in range(0, days, 7):
            week += 1
        return week

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name = ""
        description = ""
        weeks = 0
        for key, value in course_dict.items():
            if key == "name":
                name = value
            elif key == "description":
                description = value
            elif key == "days":
                weeks = cls.days_to_weeks(value)
        return cls(name, description, weeks)
