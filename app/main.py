from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days) -> int:
        """" 1 day = 0,142857143 week"""
        if days % 7 == 0:
            weeks = days // 7
        else:
            weeks = ceil(days * 0.142857143)
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return OnlineCourse(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
