class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, curs_dict: dict) -> object:
        name = curs_dict["name"]
        description = curs_dict["description"]
        weeks = cls.days_to_weeks(curs_dict["days"])
        return cls(name, description, weeks)
