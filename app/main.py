import math

class OnlineCourse:

    @classmethod
    def from_dict(cls, course_dict: dict) -> cls:
    	return OnlineCourse(course_dict["name"], course_dict["description"], 
                            cls.days_to_weeks(course_dict["days"]))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks
        
