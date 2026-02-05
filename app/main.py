import math


class OnlineCourse:

    def __init__(self,
                 name: str,
                 description: str,
                 weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, my_dict: dict) -> any:
        return OnlineCourse(my_dict["name"],
                            my_dict["description"],
                            cls.days_to_weeks(my_dict["days"]))
