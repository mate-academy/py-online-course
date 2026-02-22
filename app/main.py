from typing import Dict, Any


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name: str = name
        self.description: str = description
        self.weeks: int = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks: int = days // 7
        if days % 7 != 0:
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: Dict[str, Any]) -> "OnlineCourse":
        name: str = course_dict["name"]
        description: str = course_dict["description"]
        days: int = course_dict["days"]
        weeks: int = cls.days_to_weeks(days)
        return cls(name=name, description=description, weeks=weeks)
