class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        result = days // 7
        remainder = days % 7
        if remainder > 0:
            result += 1
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "OnlineCourse":
        return cls(
            name=data["name"],
            description=data["description"],
            weeks=OnlineCourse.days_to_weeks(data["days"]),
        )
