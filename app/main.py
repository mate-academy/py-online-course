class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.days = weeks * 7

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days < 7:
            return 1
        if days % 7 == 0:
            return days // 7
        if days % 7 >= 1:
            return days // 7 + 1
        else:
            return days // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], weeks)
