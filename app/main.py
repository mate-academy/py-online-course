from __future__ import annotations


class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

        self.course_dict["name"] = name
        self.course_dict["description"] = description
        self.course_dict["weeks"] = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days == 0:
            return 0
        if days < 7 and days != 0:
            return 1
        elif days > 7 and days % 7 != 0:
            return days // 7 + 1
        return days // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        count_weeks = OnlineCourse.days_to_weeks(course_dict.get("days"))
        return cls(
            course_dict.get("name"),
            course_dict.get("description"),
            count_weeks
        )
