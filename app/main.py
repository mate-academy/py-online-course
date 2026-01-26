import math
from typing import Dict, Any, Self

class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> Self:
    	return cls(course_dict["name"], course_dict["description"], 
                            cls.days_to_weeks(course_dict["days"]))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)


        
