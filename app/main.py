from __future__ import annotations
import math
from typing import Any


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        # Переводимо дні в тижні з округленням до більшого цілого числа
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict[str, Any]) -> OnlineCourse:
        # Конвертуємо тривалість за допомогою нашого статичного методу
        weeks_duration = cls.days_to_weeks(course_dict["days"])

        # Повертаємо новий екземпляр класу
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks_duration,
        )
