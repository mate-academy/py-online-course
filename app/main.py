class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.course_dict = self.make_a_dict()

    @staticmethod
    def days_to_weeks(days: int) -> int:
        less = days % 7
        ful_week = (days // 7)
        if less > 0:
            return ful_week + 1
        else:
            return ful_week

    def make_a_dict(self) -> dict:
        course_dict = {
            "name" : self.name,
            "description": self.description,
            "days": self.weeks * 7
        }
        return course_dict

    @classmethod
    def from_dict(cls, course_dict: dict) -> None:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
