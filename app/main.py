class OnlineCourse:
    def __init__(self, name: str, description: str, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return days // 5

    @classmethod
    def from_dict(cls, course_dict: dict):
        name = course_dict['name']
        description = course_dict['description']
        weeks = OnlineCourse.days_to_weeks(course_dict['days'])
        return cls(name, description, weeks)
