from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Convert days to weeks, rounding up to cover partial weeks.

        Examples:
            days_to_weeks(10) == 2
            days_to_weeks(14) == 2
            days_to_weeks(15) == 3
        """
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """
        Create an OnlineCourse instance from a dictionary with keys:
        "name", "description", and "days" (duration in days).
        """
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name=name, description=description, weeks=weeks)


if __name__ == "__main__":
    course_dict = {
        "name": "Python Core",
        "description": (
            "After this course you will know everything about Python and "
            "how to use it professionally in many fields."
        ),
        "days": 12,
    }

    python_course = OnlineCourse.from_dict(course_dict)
    print(python_course.weeks)  # Output: 2

    # Output:
    # After this course you will know everything about Python and how to
    # use it professionally in many fields.
    print(python_course.description)
