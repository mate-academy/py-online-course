from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Calculating the number of weeks using the formula 'days / 7'
        """
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        """
        Returning new instance of OnlineCourse with correct attributes
        using staticmethod days_to_weeks
        """
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], weeks)
