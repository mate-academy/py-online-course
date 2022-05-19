from math import ceil


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(day):
        return ceil(day / 7)

    @classmethod
    def from_dict(cls, course_dict):
        cls.name = course_dict["name"]
        cls.description = course_dict["description"]
        cls.weeks = cls.days_to_weeks(course_dict["days"])
        return cls(cls.name, cls.description, cls.weeks)
