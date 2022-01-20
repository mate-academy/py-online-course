import math


class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return math.ceil(days / 7) if days > 7 else 1

    @classmethod
    def from_dict(cls, course_dict):
        arr = []
        for value in course_dict.values():

            if course_dict.get('name'):
                arr.append(value)

            elif course_dict.get('description'):
                arr.append(value)

            elif course_dict.get('days'):
                arr.append(value)

        return cls(arr[0], arr[1], cls.days_to_weeks(arr[2]))
