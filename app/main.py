class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        if days % 7 > 0:
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        return cls(course_dict.get("name"), course_dict.get("description")
                   , cls.days_to_weeks(course_dict.get("days")))
