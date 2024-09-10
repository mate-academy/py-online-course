class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        result = int(days / 7) if days % 7 == 0 else int(days / 7) + 1
        print(result)
        return result

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], weeks)
