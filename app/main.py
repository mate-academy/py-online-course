class OnlineCourse:
    new_dict = {}

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        weeks = 0
        while days > 0:
            weeks += 1
            days -= 7
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict):
        weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], weeks)
