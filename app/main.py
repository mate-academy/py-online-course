from typing import Self


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @ staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 != 0:
            weeks = days // 7 + 1
            return weeks
        else:
            weeks = days // 7
            return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> Self:
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name, description, weeks)
