from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        full_week = days // 7
        if days % 7 > 0:
            full_week += 1
        return full_week

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        course = OnlineCourse(name=course_dict["name"],
                              description=course_dict["description"],
                              weeks=cls.days_to_weeks(course_dict["days"])
                              )
        return course
