from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            course_dict.get("name"),
            course_dict.get("description"),
            cls.days_to_weeks(course_dict.get("days"))
            if course_dict.get("days") else course_dict.get("weeks")
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 != 0:
            weeks = (days // 7) + 1
        else:
            weeks = days / 7
        return int(weeks)
