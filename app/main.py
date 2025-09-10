from __future__ import annotations


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.course_dict["name"] = self.name
        OnlineCourse.course_dict["description"] = self.description
        OnlineCourse.course_dict["days"] = self.weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if 7 > days > 0:
            return 1
        count = days // 7
        if days > 7 * count:
            return count + 1
        return count

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name = course_dict["name"]
        description = course_dict["description"]
        days = cls.days_to_weeks(course_dict["days"])
        return cls(name, description, days)
