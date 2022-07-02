class OnlineCourse:
    def __init__(self, name: str, description: str, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        return days // 5

    @classmethod
    def from_dict(cls, course_dict: dict):
        for _ in course_dict:
            new_weeks = cls.days_to_weeks(course_dict['days'])
            return cls(course_dict["name"], 
                       course_dict["description"], 
                       new_weeks)
