from __future__ import annotations

class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return OnlineCourse(course_dict["name"], course_dict["description"],
                            cls.days_to_weeks(int(course_dict["days"])))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days // 7 if days % 7 == 0 else days // 7 + 1
