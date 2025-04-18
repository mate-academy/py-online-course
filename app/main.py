from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(day: int) -> int:
        weeks = 0
        if day % 7 != 0:
            weeks = day // 7 + 1
        else:
            weeks = day // 7
        return weeks

    @classmethod
    def from_dict(cls, data: dict) -> OnlineCourse:
        return cls(
            name=data["name"],
            description=data["description"],
            weeks=cls.days_to_weeks(data["days"])
        )
