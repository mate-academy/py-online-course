class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "weeks": self.weeks,
        }

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 == 0:
            weeks = days / 7
        elif days % 7 != 0:
            weeks = days // 7 + 1
        return int(weeks)

    @classmethod
    def from_dict(cls, data: dict) -> "OnlineCourse":
        name = data["name"]
        description = data["description"]
        days = data["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
