import math


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        print("check this ", course_dict['name'])
        weeks = cls.days_to_weeks(course_dict['days'])
        course = cls(course_dict['name'], course_dict['description'], weeks)
        OnlineCourse.OnlineClass = course
        return course
