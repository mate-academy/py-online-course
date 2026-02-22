class OnlineCourse:
    # write your code here
    def __init__(self, name: str, description: str, weeks: int) -> list:
        self.name = name
        self.description = description
        self.weeks = weeks

    def __str(self) -> str:
        return self.description

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name=name, description=description, weeks=weeks)
