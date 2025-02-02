from __future__ import annotations
import math


class OnlineCourse:
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7.0)
    pass

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    def from_dict(course: dict) -> OnlineCourse:
        return OnlineCourse(course["name"],
                            course["description"],
                            OnlineCourse.days_to_weeks(course["days"]))
