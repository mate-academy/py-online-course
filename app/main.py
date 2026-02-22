class OnlineCourse:

    course_dict = {}

    def __init__(
            self,
            name: str,
            description: str,
            weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return int(-1 * (days / 7) // 1 * -1)

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        return cls(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(course_dict["days"])
        )
