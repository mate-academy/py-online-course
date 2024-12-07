class OnlineCourse:
    # Метод __init__ для ініціалізації об'єкта класу
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    # Статичний метод для конвертації днів у тижні
    @staticmethod
    def days_to_weeks(days):
        # Округлення вгору для врахування неповного тижня
        return (days + 6) // 7

    # Класовий метод для створення об'єкта на основі словника
    @classmethod
    def from_dict(cls, course_dict):
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)  # Використовуємо days_to_weeks для конвертації
        return cls(name, description, weeks)  # Створюємо новий об'єкт класу
