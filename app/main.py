from math import ceil


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict):
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = course_dict.get("weeks", cls.days_to_weeks(course_dict["days"]))

        return cls(name, description, weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)
