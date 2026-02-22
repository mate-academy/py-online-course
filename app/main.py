from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        counter = 0
        while days > 7:
            days -= 7
            counter += 1
        if days > 0:
            counter += 1
        return counter

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(course_dict.get("name"),
                   course_dict.get("description"),
                   cls.days_to_weeks(course_dict.get("days")))
