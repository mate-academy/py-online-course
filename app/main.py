class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return days // 7 if days % 7 == 0 else (days // 7 + 1)

    @classmethod
    def from_dict(cls, course_dict):
        name = course_dict["name"]
        description = course_dict["description"]
        week = cls.days_to_weeks(course_dict["days"])
        return cls(name, description, week)
