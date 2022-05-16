class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        return days / 7 if days % 7 == 0 else days // 7 + 1

    @classmethod
    def from_dict(cls, course: dict):
        return OnlineCourse(
            course["name"], course["description"], cls.days_to_weeks(
                course["days"]
            )
        )
