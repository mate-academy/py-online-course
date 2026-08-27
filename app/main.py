class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        count_weeks = 0
        if days < 7:
            return 1
        else:
            for week in range(1, days + 1):
                if week % 7 == 0:
                    count_weeks += 1
            if days % 7 != 0:
                count_weeks += 1

            return count_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
