class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        days_to_weeks = days / 7
        if days % 7 != 0:
            days_to_weeks += 1
        return int(days_to_weeks)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        course = cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
        return course
