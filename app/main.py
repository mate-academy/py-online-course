class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        count = 0
        while days > 0:
            count += 1
            days -= 7

        OnlineCourse.weeks = count
        return OnlineCourse.weeks

    @classmethod
    def from_dict(cls, course_dict: dict):
        return cls(course_dict["name"], course_dict["description"],
                   cls.days_to_weeks(course_dict.get("days")))
