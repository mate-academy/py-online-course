from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days <= 7:
            return 1
        if (days % 7) > 0:
            result = (days // 7) + 1
        else:
            result = days / 7
        return result

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        result = cls(
            name=course_dict.get("name"),
            description=course_dict.get("description"),
            weeks=cls.days_to_weeks(course_dict.get("days"))
        )
        return result
