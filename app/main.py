class OnlineCourse:

    def __init__(
            self, name: str, description: str, weeks: int | float
    ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(count_days: int) -> int:
        result = 0
        while count_days > 0:
            result += 1
            count_days -= 7
        return result

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        if course_dict.get("days"):
            course_dict.update(
                {"weeks": OnlineCourse.days_to_weeks(course_dict["days"])}
            )
        return cls(
            course_dict["name"], course_dict["description"],
            course_dict["weeks"]
        )
