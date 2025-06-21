class OnlineCourse:
    def __init__(self, name: str,
                 description: str,
                 weeks: int | float) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    def __str__(self) -> str:
        return self.description

    @staticmethod
    def days_to_weeks(days: int) -> int:
        result = days / 7
        return result if result == int(result) else int(result) + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return cls(course_dict["name"],
                   course_dict["description"],
                   cls.days_to_weeks(course_dict["days"]))
