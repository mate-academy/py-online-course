from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days // 7 if days % 7 == 0 else (days // 7) + 1

    @classmethod
    def from_dict(cls, cource_dict: dict) -> OnlineCourse:
        return cls(
            name=cource_dict["name"],
            description=cource_dict["description"],
            weeks=cls.days_to_weeks(cource_dict["days"])
        )
