from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    def __str__(self):
        return self

    @staticmethod
    def days_to_weeks(days: int):
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        days = course_dict["days"]
        return OnlineCourse(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(days)
        )
