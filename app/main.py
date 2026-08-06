class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days < 7:
            return 1
        elif days % 7 == 0:
            week = days // 7
        else:
            week = days // 7 + 1
        return week

    @classmethod
    def from_dict(cls, course_dict):
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
