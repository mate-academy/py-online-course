from __future__ import annotations


class OnlineCourse:
    def __init__(
        self,
        name: str,
        description: str,
        weeks: int
    ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course: dict) -> OnlineCourse:
        return cls(
            name=course.get("name"),
            description=course.get("description"),
            weeks=cls.days_to_weeks(course.get("days"))
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days / 7 if days % 7 == 0 else days // 7 + 1
