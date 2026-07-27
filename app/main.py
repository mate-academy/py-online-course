class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days % 7 != 0:
            return days // 7 + 1
        return days // 7

    @classmethod
    def from_dict(cls, course_dict):
        name = course_dict.get('name')
        description = course_dict.get('description')
        weeks = cls.days_to_weeks(course_dict.get('days', 0))
        return cls(name, description, weeks)
