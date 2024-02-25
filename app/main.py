from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            course_dict["name"],
            course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
