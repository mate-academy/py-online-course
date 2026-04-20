class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        dict_name = course_dict["name"]
        dict_description = course_dict["description"]
        dict_weeks = cls.days_to_weeks(course_dict["days"])
        return cls(dict_name, dict_description, dict_weeks)
