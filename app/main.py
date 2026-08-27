from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days / 7 > days // 7:
            return days // 7 + 1
        return days // 7

    @classmethod
    def from_dict(cls, dicts: dict) -> OnlineCourse:
        temp = cls.days_to_weeks(dicts["days"])
        return cls(dicts["name"], dicts["description"], temp)
