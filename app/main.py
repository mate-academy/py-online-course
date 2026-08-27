class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # Convert days to weeks (ceil the division)
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        # Convert days to weeks using the static method
        weeks = cls.days_to_weeks(course_dict["days"])
        # Return a new instance of OnlineCourse
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
