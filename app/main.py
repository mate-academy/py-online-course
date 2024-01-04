class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int | None:
        if days < 7:
            return 1
        elif days == 0:
            return None
        else:
            number = days // 7
            result = days - (number * 7)
            if 0 < result < 7:
                return number + 1
            return number

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        name = course_dict.get("name")
        description = course_dict.get("description")
        weeks = cls.days_to_weeks(course_dict.get("days"))
        return cls(name, description, weeks)
