class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        # Initialize the course attributes
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # Convert days to weeks (rounding up for partial weeks)
        return (days + 6) // 7  # Equivalent to math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        # Extract name and description from the dictionary
        name = course_dict["name"]
        description = course_dict["description"]
        # Convert days to weeks using the static method
        weeks = cls.days_to_weeks(course_dict["days"])
        # Create and return a new instance of OnlineCourse
        return cls(name, description, weeks)
