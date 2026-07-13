class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(day):
        week = (day + 6) // 7
        return week

    @classmethod
    def from_dict(cls, course_dict):
        name = course_dict["name"]
        description = course_dict["description"]
        day = course_dict["days"]
        weeks = cls.days_to_weeks(day)
        return cls(name, description, weeks)
