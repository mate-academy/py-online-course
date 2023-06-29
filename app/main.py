class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = days // 7
        if days % 7 > 0:
            week += 1
        return week

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
