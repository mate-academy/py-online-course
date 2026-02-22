class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    def __repr__(self) -> str:
        return (f"Online course: {self.name}, "
                f"Description: {self.description}, "
                f"Weeks: {self.weeks}")

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name, description, weeks)

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7
