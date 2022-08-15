class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        temp_dict = {1: range(0, 8), 2: range(8, 15), 3: range(15, 22),
                     4: range(22, 29), 5: range(29, 36), 6: range(36, 43),
                     7: range(43, 50), 8: range(50, 57), 9: range(57, 64),
                     10: range(64, 71), 11: range(71, 78), 12: range(78, 85),
                     13: range(85, 92), 14: range(92, 99), 15: range(99, 106),
                     16: range(106, 113), 17: range(113, 120),
                     18: range(120, 127)}
        for key, value in temp_dict.items():
            if days in value:
                return key

        # import math
        # return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict):
        return cls(
            course_dict["name"],
            course_dict["description"],
            OnlineCourse.days_to_weeks(course_dict["days"])
        )
