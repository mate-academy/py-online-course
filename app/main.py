class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if (days % 7) == 0:
            return days // 7
        else:
            return (days // 7) + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
