class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict.get("name", "")
        description = course_dict.get("description", "")
        days = course_dict.get("days", 0)
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)

    @classmethod
    def days_to_weeks(cls, days: int) -> int:
        if days % 7 == 0:
            return days / 7.0
        else:
            return round(days // 7.0 + 1)
