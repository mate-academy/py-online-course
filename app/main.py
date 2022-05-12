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
    def from_dict(self, course_dict):
        self.name = course_dict["name"]
        self.description = course_dict["description"]
        self.weeks = self.days_to_weeks(course_dict["days"])
        return OnlineCourse(self.name, self.description, self.weeks)
