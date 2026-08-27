class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Invalid days value.")
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        required_fields = {"name", "description", "days"}
        missing = required_fields - course_dict.keys()
        if missing:
            raise ValueError(f"Missing fields in course_dict: {missing}")
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
