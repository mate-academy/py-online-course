class OnlineCourse:
    # ініціалізація класа
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7
# Цей метод створює новий екземпляр класу
# OnlineCourse з використанням інформації з словника course_dict

    @classmethod
    def from_dict(cls, course_dict: dict) -> callable:
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name, description, weeks)
