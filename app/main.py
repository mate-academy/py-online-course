class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days % 7 == 0:
            return days / 7
        else:
            return days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict):
        days = course_dict["days"]
        return OnlineCourse(course_dict["name"],
                            course_dict["description"],
                            OnlineCourse.days_to_weeks(days))
