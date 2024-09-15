class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict):
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return cls(name, description, weeks)

    @staticmethod
    def days_to_weeks(days):
        weeks = 1
        while days > 7:
            days -= 7
            weeks += 1
        return weeks
