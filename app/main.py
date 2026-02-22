class OnlineCourse:
    def __init__(self,
                 name: str,
                 description: str,
                 weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        if days % 7:
            return days // 7 + 1
        return days // 7

    @classmethod
    def from_dict(cls, course_dict: dict):
        return OnlineCourse(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
