from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = int(days / 7) if days % 7 == 0 else days // 7 + 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        if "days" in course_dict:
            course_dict["weeks"] = cls.days_to_weeks(course_dict["days"])
            course_dict.pop("days")
        return cls(**course_dict)
