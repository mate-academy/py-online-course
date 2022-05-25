class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks
        self.course_dict = {
            "name": name,
            "description": description,
            "weeks": weeks
        }

    @staticmethod
    def days_to_weeks(days):
        if days % 7 == 0:
            return days // 7
        else:
            return (days + 7) // 7

    @classmethod
    def from_dict(cls, course_dict):
        return OnlineCourse(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )
