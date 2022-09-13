class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int,):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return int(-1 * (days / 7) // 1 * -1)

    @classmethod
    def from_dict(cls, course_dict: dict):
        return cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
