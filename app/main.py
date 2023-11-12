from typing import Dict


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: Dict[str, str]) -> "OnlineCourse":
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name=name, description=description, weeks=weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ((days + 6) // 7)
