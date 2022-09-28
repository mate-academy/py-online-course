class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        import math
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict):
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=cls.days_to_week(course_dict["days"])
                   )
