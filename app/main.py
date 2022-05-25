class OnlineCourse:
    """class OnlineCourse takes name, description,
    weeks.This class has a static method 'days_to_week'
    which takes days and convert this number to week.
    Class method 'from_dict'  takes parameters cls and course_dict,
    use method 'days_to_week' to convert days to weeks
    and return new instance with correct attributes"""
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        if days % 7 == 0:
            return days / 7
        elif days < 7:
            return 1
        return (days // 7) + 1

    @classmethod
    def from_dict(cls, course_dict: dict):
        return cls(course_dict["name"], course_dict["description"],
                   OnlineCourse.days_to_weeks(course_dict["days"]))
