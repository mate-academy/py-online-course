class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict):
        weeks = cls.days_to_weeks(course_dict["days"])
        return OnlineClass(
            course_dict["name"],
            course_dict["description"],
            weeks)


class OnlineClass(OnlineCourse):
    def __init__(self, name: str, description: str, weeks: int):
        super().__init__(name, description, weeks)
