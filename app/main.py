from __future__ import annotations


class OnlineCourse:
    def __init__(
            self,
            name: str,
            description: str,
            weeks: int
    ):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return len(range(0, days, 7))

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return OnlineCourse(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(course_dict["days"])
        )
