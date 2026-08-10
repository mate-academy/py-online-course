class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self. description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 == 0:
            return days // 7
        return days // 7 + 1

    @classmethod
    def from_dict(cls, ndict: dict) -> classmethod:
        return cls(
            ndict["name"],
            ndict["description"],
            cls.days_to_weeks(ndict["days"])
        )
