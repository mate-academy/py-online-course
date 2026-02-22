from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        weeks = weeks + 1 if days % 7 != 0 else weeks
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        weeks = course_dict.get("weeks", "")
        if not weeks:
            weeks = OnlineCourse.days_to_weeks(course_dict.get("days", ""))
        return cls(
            name=course_dict.get("name", None),
            description=course_dict.get("description", None),
            weeks=weeks,
        )
