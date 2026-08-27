class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: str) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days - 1) // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        weeks = cls.days_to_weeks(course_dict.get("days"))
        return cls(course_dict.get("name"),
                   course_dict.get("description"),
                   weeks)
