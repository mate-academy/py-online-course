class OnlineCourse:
    @classmethod
    def from_dict(cls, course_dict):
        return OnlineCourse(name=course_dict.get("name"),
                            description=course_dict.get("description"),
                            weeks=cls.days_to_weeks(course_dict.get("days")))

    @staticmethod
    def days_to_weeks(days):
        return days // 7 if days % 7 == 0 else days // 7 + 1

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.from_dict(args[0])
        else:
            self.name = kwargs.get("name")
            self.description = kwargs.get("description")
            self.weeks = kwargs.get("weeks")
