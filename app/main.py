class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days <= 0:
            return 0
        return (days - 1) // 7 + 1

    @classmethod
    def from_dict(cls, data: dict) -> OnlineCourse:
        return cls(data["name"], data["description"],
                   cls.days_to_weeks(data["days"]))
