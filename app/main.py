class OnlineCourse:
    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.course_dict = {"name": name,
                                    "description": description,
                                    "days": weeks}

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # week have 7 days
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict.get("name")
        description = course_dict.get("description")
        days = course_dict.get("days")
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
