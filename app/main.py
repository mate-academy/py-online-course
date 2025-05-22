class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: str) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return days // 7 + 1 if days % 7 != 0 else days // 7

    @classmethod
    def from_dict(cls, data: dict) -> "OnlineCourse":
        name = data["name"]
        description = data["description"]
        weeks = cls.days_to_weeks(data["days"])
        return cls(name, description, weeks)
