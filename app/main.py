from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days // 7) + 1 if days % 7 != 0 else days // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        course_info = list(course_dict.values())
        return cls(
            course_info[0],
            course_info[1],
            OnlineCourse.days_to_weeks(course_info[2])
        )
