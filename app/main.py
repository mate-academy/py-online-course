from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course: dict) -> "OnlineCourse":
        return cls(course["name"],
                   course["description"],
                   cls.days_to_weeks(course["days"]))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)
