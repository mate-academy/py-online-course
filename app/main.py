from math import ceil


class OnlineCourse:
    def __init__(self,
                 name,
                 description,
                 weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        week = days / 7
        return ceil(week)

    @classmethod
    def from_dict(cls, course_dict):
        course = cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
        return course
