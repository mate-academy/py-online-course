from __future__ import annotations


class OnlineClass:
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
    def from_dict(
            cls,
            course_dict: dict
    ) -> OnlineClass:
        return OnlineClass(
            course_dict.get("name"),
            course_dict.get("description"),
            cls.days_to_weeks(course_dict.get("days"))
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 != 0:
            return int(days / 7) + 1

        return int(days / 7)
