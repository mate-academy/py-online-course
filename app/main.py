class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        weeks = days // 7
        if days % 7 != 0:
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict):
        name = course_dict['name']
        description = course_dict['description']
        weeks = OnlineCourse.days_to_weeks(course_dict['days'])
        return cls(name, description, weeks)
