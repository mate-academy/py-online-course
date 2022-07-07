class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict):
        return OnlineCourse(name=course_dict["name"],
                            description=course_dict["description"],
                            weeks=cls.days_to_weeks(course_dict["days"]))

    @staticmethod
    def days_to_weeks(days):
        week = days // 7
        if days % 7 > 0:
            week += 1
        return week
