from __future__ import annotations

import math
from typing import Union


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int
                 ) -> OnlineCourse:

        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        print(course_dict)
        for key, value in course_dict.items():
            instance_name = course_dict["name"]
            instance_description = course_dict["description"]
            instance_weeks = course_dict["days"]
        return cls(
            instance_name, instance_description,
            cls.days_to_weeks(instance_weeks))

    @staticmethod
    def days_to_weeks(days: Union[int, float]) -> int:
        if days % 7 != 0:
            return int(math.floor(days / 7 + 1))
        return int(days / 7)
