class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """Convert days to weeks, rounding up for partial weeks."""
        return -(-days // 7)  # Ceiling division

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """Create an OnlineCourse instance from a dictionary."""
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"]),
        )
