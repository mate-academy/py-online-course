class OnlineCourse:
    def __init__(
        self,
        name: str,
        description: object,
        weeks: int
    ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # Calculate weeks by dividing days by 7 and rounding up
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: object) -> object:
        # Extract values from the dictionary
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        # Convert days to weeks using the static method
        weeks = cls.days_to_weeks(days)
        # Return a new instance of OnlineCourse
        return cls(name, description, weeks)
