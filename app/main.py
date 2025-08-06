class OnlineClass:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        if days % 7 != 0:
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineClass":
        days = course_dict.get("days")
        name = course_dict.get("name")
        description = course_dict.get("description")
        weeks = cls.days_to_weeks(days)

        return OnlineCourse(name, description, weeks)
