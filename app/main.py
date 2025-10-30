from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 == 0:
            return int(days / 7)
        return int((days // 7) + 1)

    @classmethod
    def from_dict(cls, course_dict: dict[str, str | int]) -> OnlineCourse:
        days = OnlineCourse.days_to_weeks(course_dict["days"])
        new_course = cls(course_dict["name"],
                         course_dict["description"],
                         days)
        return new_course
