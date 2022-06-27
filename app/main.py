import math


class OnlineCourse:

    weeks = 0

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7)

    @staticmethod
    def from_dict(course_dict):
        OnlineCourse.weeks = OnlineCourse.days_to_weeks(course_dict['days'])
        return OnlineCourse(course_dict['name'],
                            course_dict['description'], OnlineCourse.weeks)
