class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        week = days // 7
        if days % 7 > 0:
            week += 1
        return week

    @classmethod
    def from_dict(cls, course: dict):
        return cls(course['name'], course['description'],
                   OnlineCourse.days_to_weeks(course['days']))
