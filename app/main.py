from __future__ import annotations


class OnlineCourse:
    # write your code here
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 == 0:
            weeks_left = days // 7
        else:
            weeks_left = days // 7 + 1
        return weeks_left

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        new_object = cls(course_dict["name"], course_dict["description"],
                         weeks)
        return new_object
