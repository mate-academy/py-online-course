class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, it_course: dict) -> OnlineCourse:
        return cls(it_course["name"], it_course["description"],
                   cls.days_to_weeks(it_course["days"]))
