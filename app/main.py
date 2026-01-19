class OnlineCourse:
    def __init__(self, name : str, description : str, weeks : int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days : int) -> int:
        if days % 7 != 0:
            return 1 + days // 7
        elif days % 7 == 0:
            return int(days / 7)
        return 0

    @classmethod
    def from_dict(cls, course_dict : dict) -> object:
        return cls(course_dict["name"],
                   course_dict["description"],
                   cls.days_to_weeks(course_dict["days"]))
