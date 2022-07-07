from math import ceil


class OnlineCourse:
    DAYS_IN_WEEKS = 7

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days < 0:
            return 0
        else:
            return int(ceil(days / OnlineCourse.DAYS_IN_WEEKS))

    @classmethod
    def from_dict(cls, dictionary):
        if 'days' in dictionary:
            return cls(
                dictionary['name'],
                dictionary['description'],
                cls.days_to_weeks(dictionary['days']),
            )
        elif 'weeks' in dictionary:
            return cls(
                dictionary['name'],
                dictionary['description'],
                dictionary['weeks'],
            )
