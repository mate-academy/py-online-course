class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        our_weeks = days // 7
        if days % 7 != 0:
            our_weeks += 1
        return our_weeks

    @classmethod
    def from_dict(cls, dict_in: dict) -> "OnlineCourse":
        our_online_course = cls(
            dict_in["name"],
            dict_in["description"],
            cls.days_to_weeks(dict_in["days"])
        )
        return our_online_course
