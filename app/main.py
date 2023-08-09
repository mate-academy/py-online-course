from math import ceil
from typing import Type, TypeVar

Self = TypeVar("Self", bound="OnlineCourse")


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name: str = name
        self.description: str = description
        self.weeks: int = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls: Type[Self], course_dict: dict) -> Self:
        weeks: int = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], weeks)
