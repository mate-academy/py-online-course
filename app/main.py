class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> callable:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = 1
        for i in range(7, days, 7):
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> callable:
        return cls(name=course_dict["name"]
                   , description=course_dict["description"]
                   , weeks=cls.days_to_weeks(course_dict["days"])
                   )
