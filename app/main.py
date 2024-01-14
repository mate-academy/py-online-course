from __future__ import annotations


class OnlineCourse:
    def __init__(self, name : str, description : str, weeks : int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(day: int) -> int:
        return (day + 6) // 7

    @classmethod
    def from_dict(cls, course_dict : dict) -> OnlineCourse:
        week = cls.days_to_weeks(course_dict["days"])
        course = cls(course_dict["name"], course_dict["description"], week)
        return course
