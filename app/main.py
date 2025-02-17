class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # Convert days to weeks, rounding up if there are remaining days
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> 'OnlineCourse':
        # Extract name and description from the dictionary
        name: str = course_dict["name"]
        description: str = course_dict["description"]
        # Convert days to weeks using the static method
        weeks: int = cls.days_to_weeks(course_dict["days"])
        # Return a new instance of OnlineCourse
        return cls(name, description, weeks)
