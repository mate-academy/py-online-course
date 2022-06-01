from math import ceil


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks
        self.days_to_weeks(13)

    @classmethod
    def from_dict(cls, course_dict):
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=cls.days_to_weeks(course_dict["days"]))

    @staticmethod
    def days_to_weeks(days):
        return ceil(days / 7)
