import math
from typing import Optional, Type


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days_number: int) -> int:
        return math.ceil(days_number / 7)

    @classmethod
    def from_dict(
        cls,
        course_dict: dict,
        course_class: Optional[Type["OnlineCourse"]] = None
    ) -> "OnlineCourse":
        if course_class is None:
            course_class = cls
        return course_class(course_dict["name"],
                            course_dict["description"],
                            cls.days_to_weeks(course_dict["days"]))
