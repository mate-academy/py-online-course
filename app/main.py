class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.course = self

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        if days % 7 != 0:
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> type:
        if "weeks" in course_dict:
            return cls(course_dict["name"]
                       , course_dict["description"], course_dict["weeks"])
        elif "days" in course_dict:
            return cls(course_dict["name"]
                       , course_dict["description"]
                       , cls.days_to_weeks(course_dict["days"]))
