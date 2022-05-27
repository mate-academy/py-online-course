class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 == 0:
            return int(days / 7)
        else:
            return int(days / 7) + 1

    @classmethod
    def from_dict(cls, course_dict):
        new_weeks = cls.days_to_weeks(course_dict['days'])
        del course_dict['days']
        course_dict['weeks'] = new_weeks
        new_names = course_dict['name']
        new_description = course_dict['description']
        return OnlineCourse(new_names, new_description, new_weeks)
