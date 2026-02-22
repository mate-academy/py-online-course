class OnlineCourse:

    course_dict = {}

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.course_dict.update({
            "name": self.name,
            "description": self.description,
            "days": self.weeks
        })

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 == 0:
            return days // 7
        return days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> dict:
        print(type(cls("Python", "Best", 56)))
        cls.correct_course_dict = cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict.popitem()[1])
        )
        print(type(cls.correct_course_dict))
        return cls.correct_course_dict
