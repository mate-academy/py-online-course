from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days < 7:
            return 1
        if days % 7:
            return days // 7 + 1
        else:
            return days // 7

    @classmethod
    def from_dict(cls, c_dict: dict) -> OnlineCourse:
        return cls(name=c_dict["name"],
                   description=c_dict["description"],
                   weeks=OnlineCourse.days_to_weeks(c_dict["days"]))
