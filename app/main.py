from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # 1 day == 0.142857 weeks
        return ceil(days * 0.142857)

    @classmethod
    def from_dict(cls, course_dict: dict) -> dict:
        course_info = course_dict.copy()
        number_of_weeks = cls.days_to_weeks(course_info["days"])
        course_info.pop("days")
        course_info["weeks"] = number_of_weeks

        name = course_info["name"]
        description = course_info["description"]
        weeks = course_info["weeks"]

        return cls(name, description, weeks)
