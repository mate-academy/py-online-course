class OnlineCourse:

    def __init__(
            self, name: str = "Unknown",
            description: str = "None",
            weeks: int = None,
            course_dict: dict = None
    ) -> None:
        if course_dict:
            self.name = course_dict.get("name")
            self.description = course_dict.get("description")
            self.weeks = OnlineCourse.days_to_weeks(course_dict.get("days"))
            return
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Return weeks from days, even if week is not complete
        :param days:
        :return:
        """
        return int(days // 7 + 1) if days % 7 != 0 else int(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return cls(course_dict=course_dict)
