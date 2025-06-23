from __future__ import annotations


class OnlineCourse:
    def __init__(
        self,
        name: str,
        description: str,
        weeks: int
    ) -> None:
        if not isinstance(name, str):
            raise TypeError(
                f"Unsupported type for name: {type(name).__name__}"
            )
        self.name = name

        if not isinstance(description, str):
            raise TypeError(
                f"Unsupported type for"
                f"description: {type(description).__name__}"
            )
        self.description = description

        if not isinstance(weeks, int):
            raise TypeError(
                f"Unsupported type for weeks: {type(weeks).__name__}"
            )
        self.weeks = weeks

    @classmethod
    def days_to_weeks(cls, days: int) -> int:
        if not isinstance(days, int):
            raise TypeError(f"Unsupported type: {type(days).__name__}")
        return days // 7 + (1 if days % 7 != 0 else 0)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            course_dict.get("name", ""),
            course_dict.get("description", ""),
            cls.days_to_weeks(course_dict.get("days", 0))
        )
