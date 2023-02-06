class OnlineCourse:
    def __init__(self,
                 name: str,
                 description: str,
                 weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        if days % 7 != 0:
            weeks = weeks + 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> None:
        return cls(course_dict["name"],
                   course_dict["description"],
                   OnlineCourse.days_to_weeks(course_dict["days"]))
