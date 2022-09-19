class OnlineCourse:
    def __init__(
            self,
            name: str,
            description: str,
            weeks: int
    ):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = 1
        if days > 7:
            if days % 7 != 0:
                weeks += days // 7
            else:
                weeks = days // 7
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict):
        weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
