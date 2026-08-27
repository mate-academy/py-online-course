from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days // 7 if days % 7 == 0 else days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            **{key if key != "days"
               else "weeks": course_dict[key]
               if key != "days"
               else OnlineCourse.days_to_weeks(course_dict[key])
               for key in course_dict})
