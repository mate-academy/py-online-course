class OnlineCourse:
    @classmethod
    def from_dict(cls, course_dict):
        return cls(course_dict.get("name"),
                   course_dict.get("description"),
                   cls.days_to_weeks(course_dict.get("days")))

    @staticmethod
    def days_to_weeks(days):
        return days // 7 if days % 7 == 0 else days // 7 + 1

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks
