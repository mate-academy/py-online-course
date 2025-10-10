import math

class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Converts days to weeks, rounding up the last week.
        Example: 14 days -> 2 weeks; 15 days -> 3 weeks.
        """
        # Використовуємо math.ceil для округлення до більшого цілого числа
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> 'OnlineCourse':
        """
        Creates an OnlineCourse instance from a dictionary.
        """
        # 1. Конвертуємо дні у тижні за допомогою days_to_weeks
        weeks = cls.days_to_weeks(course_dict["days"])

        # 2. Створюємо та повертаємо новий екземпляр класу
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks,
        )
