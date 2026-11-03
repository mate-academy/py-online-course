class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, dictionary: dict) -> "OnlineCourse":
        name, description, days = (dictionary.get("name"),
                                   dictionary.get("description"),
                                   dictionary.get("days"))
        return cls(name, description, cls.days_to_weeks(days))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if (days % 7) > 0:
            return round(days / 7 + 0.5)
        return round(days / 7)
