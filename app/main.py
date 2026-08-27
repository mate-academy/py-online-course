class OnlineCourse:
    # write your code here
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        count = 0
        if days % 7 == 0:
            count = days // 7
        elif days % 7 != 0:
            count = days // 7 + 1
        return count

    @classmethod
    def from_dict(cls, course_dict: dict) -> callable:
        return cls(course_dict["name"], course_dict["description"],
                   OnlineCourse.days_to_weeks(course_dict["days"]))
