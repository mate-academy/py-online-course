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

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, dictitonary: dict) -> OnlineCourse:
        return cls(
            dictitonary["name"],
            dictitonary["description"],
            cls.days_to_weeks(dictitonary["days"])
        )
