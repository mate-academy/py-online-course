class OnlineCourse:
    def __init__(self, name: int, description: int, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: int):
        name = course_dict['name']
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
