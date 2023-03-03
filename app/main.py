class OnlineCourse:

    def __init__(self, name: str, description: str,
                 weeks: int) -> "OnlineCourse":
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # 1 week = 7 days
        if days % 7 > 0:
            return days // 7 + 1
        else:
            return days // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        cls.name = course_dict["name"]
        cls.description = course_dict["description"]
        cls.weeks = cls.days_to_weeks(course_dict["days"])
        return cls
