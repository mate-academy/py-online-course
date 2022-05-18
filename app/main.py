from math import ceil


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        weeks = ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict):
        return OnlineCourse(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
