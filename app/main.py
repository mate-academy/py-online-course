from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if not isinstance(days, int):
            raise TypeError("days must be an integer.")
        return -(-days // 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        if not isinstance(course_dict, dict):
            raise TypeError("course_dict must be a dictionary.")
        required_keys = ["name", "description", "days"]
        for key in required_keys:
            if key not in course_dict:
                raise ValueError(f"Missing required key: {key}")
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        if not isinstance(name, str):
            raise TypeError(f"Expected 'name' "
                            f"to be a string, got {type(name).__name__}.")
        if not isinstance(description, str):
            raise TypeError(f"Expected 'description' to be a string, "
                            f"got {type(description).__name__}.")
        if not isinstance(days, int):
            raise TypeError(f"Expected 'days' "
                            f"to be an integer, got {type(days).__name__}.")
        weeks = cls.days_to_weeks(days)
        return cls(name=name, description=description, weeks=weeks)
