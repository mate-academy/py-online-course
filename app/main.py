import math


class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        full_weeks = 0
        if days <= 7:
            return 1
        else:
            full_weeks = days / 7
            return math.ceil(full_weeks)

    @classmethod
    def from_dict(cls, course_dict):
        days = course_dict['days']
        weeks = cls.days_to_weeks(days)
        the_instance = OnlineCourse(course_dict['name'],
                                    course_dict['description'], weeks)
        return the_instance
