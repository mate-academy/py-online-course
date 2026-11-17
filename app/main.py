from __future__ import annotations


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.course_dict[name] = self.name
        OnlineCourse.course_dict[description] = self.description

    @staticmethod
    def days_to_weeks(days: int) -> int:
        OnlineCourse.course_dict[days] = days
        if days % 7 == 0:
            weeks = days // 7
        else:
            weeks = days // 7 + 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        new_course = cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
        return new_course
