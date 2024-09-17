class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict):
        res = {}

        for key, value in course_dict.items():
            res[key] = cls.days_to_weeks(value) if key == "days" else value
        return cls(res["name"], res["description"], res["days"])

    @staticmethod
    def days_to_weeks(weeks):
        return weeks // 7 + 1 if weeks % 7 != 0 else weeks // 7
