from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, dic: dict) -> OnlineCourse:
        return cls(
            name=dic["name"],
            description=dic["description"],
            weeks=cls.days_to_weeks(dic["days"])
        )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7
