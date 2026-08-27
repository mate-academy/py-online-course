class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> any:
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=cls.days_to_weeks(course_dict["days"]))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days // 7 + 1 if days % 7 else days // 7
