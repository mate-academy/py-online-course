from math import ceil


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(day):
        return ceil(day / 7)

    @staticmethod
    def from_dict(course_dict):
        return OnlineCourse(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(course_dict["days"])
        )
