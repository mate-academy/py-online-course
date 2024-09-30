class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # Calculate the number of weeks. Round up if there are leftover days.
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        # Convert days to weeks using the static method
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], weeks)
