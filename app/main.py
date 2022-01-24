class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days % 7 == 0:
            return days / 7
        return (days // 7) + 1

    @classmethod
    def from_dict(cls, course_dict):
        for key in course_dict:
            if key == "name":
                cls.name = course_dict["name"]
            if key == "description":
                cls.description = course_dict["description"]
            if key == "days":
                cls.weeks = cls.days_to_weeks(course_dict["days"])
        return cls(cls.name, cls.description, cls.weeks)
