from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return -(-days // 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        required_keys = {"name": str, "description": str, "days": int}
        for key, expected_type in required_keys.items():
            if key not in course_dict:
                raise ValueError(f">>> Missing key: '{key}' in course_dict")
            elif not isinstance(course_dict[key], expected_type):
                raise TypeError(f">>> Expected {expected_type.__name__} in '{key}' key, "
                                f"got {type(course_dict[key]).__name__} instead")
        return cls(
                course_dict["name"],
                course_dict["description"],
                OnlineCourse.days_to_weeks(course_dict["days"])
            )