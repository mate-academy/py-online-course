class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        days_count = days
        count = 0
        while days_count > 0:
            days_count -= 7
            count += 1
        return count

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return cls(
            name=course_dict.get("name", ""),
            description=course_dict.get("description", ""),
            weeks=cls.days_to_weeks(course_dict.get("days", 0))
        )
