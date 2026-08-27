class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    # Статичний метод для перетворення кількості днів на тижні
    @staticmethod
    def days_to_weeks(days: int) -> int:
        # Визначаємо кількість тижнів.
        return (days + 6) // 7
        # Це еквівалент округлення вгору до найближчого тижня.

    # Класовий метод для створення об'єкта з словника
    @classmethod
    def from_dict(cls, course_dict: dict) -> None:
        # Перетворюємо кількість днів в тижні за допомогою days_to_weeks
        weeks = cls.days_to_weeks(course_dict["days"])
        # Створюємо новий екземпляр класу, використовуючи передані дані
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
