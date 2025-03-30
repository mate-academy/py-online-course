from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_week(days: int) ->int:
        if days % 7 != 0:
            return days // 7 + 1
        return days // 7

    @classmethod
    def course_dict(cls, parameters_dict: dict) -> OnlineCourse:
        number_of_days = cls.days_to_week(parameters_dict["days"])
        return cls(
            parameters_dict["name"],
            parameters_dict["description"],
            number_of_days
        )

