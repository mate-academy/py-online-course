class OnlineCourse:
    def __init__(self, name: str | None,
                 description: str | None,
                 weeks: int | None
                 ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int | None) -> int:
        if days is None or days <= 0:
            return 0
        elif days % 7 == 0:
            return days // 7
        else:
            return days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(name=course_dict.get("name"),
                   description=course_dict.get("description"),
                   weeks=cls.days_to_weeks(course_dict.get("days"))
                   )
