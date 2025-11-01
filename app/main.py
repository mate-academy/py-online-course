import math


class OnlineCourse:
    """Класс для хранения информации об онлайн-курсе."""

    def __init__(self, name: str, description: str, weeks: int) -> None:
        """Инициализация объекта курса."""
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """Преобразует количество дней в количество недель."""
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """Создаёт экземпляр курса на основе словаря."""
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks,
        )


# ---------------- Пример использования ----------------

if __name__ == "__main__":
    course = OnlineCourse(
        name="Python Basics",
        description="The best course to start learning Python",
        weeks=2,
    )
    print(course.description)  # The best course to start learning Python

    course_dict = {
        "name": "Python Core",
        "description": (
            "After this course you will know everything about Python"
        ),
        "days": 12,
    }

    python_course = OnlineCourse.from_dict(course_dict)
    print(python_course.weeks)  # 2
