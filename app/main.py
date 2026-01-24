class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        week = 0
        while days >= 1:
            week += 1
            days = days - 7
        return week

    @classmethod
    def from_dict(cls, cours_dict: dict) -> "OnlineCourse":
        return cls(
            name=cours_dict["name"],
            description=cours_dict["description"],
            weeks=cls.days_to_weeks(cours_dict["days"])
        )
