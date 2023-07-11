from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str,
                 description: str,
                 weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return round(days / 7)
    
    @classmethod
    def dict_convert(cls, course_dict: dict) -> OnlineCourse:
        cls.course_dict = course_dict
        return cls(
            course_dict.get("name"),
            course_dict.get("description"),
            OnlineCourse.days_to_weeks(course_dict.get("days")))
