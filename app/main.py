from math import ceil


class OnlineCourse:
    def __init__(
            self,
            name: str,
            description: str,
            weeks: int
    ):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        weeks = ceil(days / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict):
        weeks = cls.days_to_weeks(course_dict["days"])
        new_class_instance = OnlineCourse(
            course_dict["name"],
            course_dict["description"],
            weeks
        )
        return new_class_instance
