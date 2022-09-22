class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days % 7 != 0:
            return int(days / 7) + 1
        return int(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        weeks = OnlineCourse.days_to_weeks(course_dict["days"])
        return OnlineCourse(course_dict["name"],
                            course_dict["description"], weeks)
