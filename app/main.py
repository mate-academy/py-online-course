from __future__ import annotations


class OnlineClass:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self. weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineClass:
        return OnlineClass(
            course_dict.get("name"),
            course_dict.get("description"),
            OnlineClass.days_to_weeks(course_dict.get("days"))
        )
