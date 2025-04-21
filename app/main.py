class OnlineCourse:
    """
    Клас для зберігання інформації про онлайн-курси.
    """

    def __init__(self, name: str, description: str, weeks: int) -> None:
        """
        Ініціалізує новий об'єкт OnlineCourse.

        Args:
            name: Назва курсу
            description: Опис курсу
            weeks: Тривалість курсу в тижнях
        """
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Перетворює кількість днів у кількість тижнів.
        Останній тиждень може бути неповним.

        Args:
            days: Кількість днів

        Returns:
            int: Кількість тижнів
        """
        # Якщо день є останнім у тижні (7, 14, 21...), то не додаємо додатковий тиждень
        if days % 7 == 0:
            return days // 7
        # Якщо є залишок днів, додаємо ще один тиждень
        else:
            return days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """
        Створює новий екземпляр OnlineCourse з словника.

        Args:
            course_dict: Словник з інформацією про курс
                {'name': str, 'description': str, 'days': int}

        Returns:
            OnlineCourse: Новий екземпляр класу OnlineCourse
        """
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]

        # Перетворюємо дні в тижні
        weeks = cls.days_to_weeks(days)

        # Створюємо новий екземпляр класу
        return cls(name=name, description=description, weeks=weeks)
