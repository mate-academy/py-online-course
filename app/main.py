from dataclasses import dataclass


@dataclass
class OnlineCourse:
    name: str
    description: str
    weeks: int

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return -(-days // 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        return cls(course_dict["name"],
                   course_dict["description"],
                   OnlineCourse.days_to_weeks(course_dict["days"]))
