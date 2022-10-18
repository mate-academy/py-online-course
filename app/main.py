class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return days // 7 + 1 if days % 7 else days // 7

    @classmethod
    def from_dict(cls, course_dict: dict):
        values_list = list(course_dict.values())
        if course_dict.get("days"):
            values_list[2] = cls.days_to_weeks(values_list[2])
        return cls(*values_list)
