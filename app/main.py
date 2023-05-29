class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        const_week = 7  # days in one week

        if days <= const_week:
            return 1
        if days % const_week == 0:
            return days // const_week
        else:
            return days // const_week + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> classmethod:
        return cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
