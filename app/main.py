import math


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, dict_course: dict) -> object:
        for info in list(dict_course):
            if info == "days":
                weeks = cls.days_to_weeks(dict_course[info])
                dict_course["weeks"] = dict_course.pop(info)
                dict_course["weeks"] = weeks
        return cls(**dict_course)
