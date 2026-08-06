class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict):
        return cls(course_dict["name"],
                   course_dict["description"],
                   cls.days_to_weeks(course_dict["days"]),
                   )

    @staticmethod
    def days_to_weeks(days):
        if days % 7 > 0:
            return days // 7 + 1
        return days // 7
