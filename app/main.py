from __future__ import annotations


class OnlineCourse:
    """
    A class to represent an online course.

    Attributes:
        name (str): The name of the course.
        description (str): A brief description of the course.
        weeks (int): The duration of the course in weeks.
    """

    def __init__(self, name: str, description: str, weeks: int) -> None:
        """
        Initializes an OnlineCourse instance.

        Args:
            name (str): The name of the course.
            description (str): A brief description of the course.
            weeks (int): The duration of the course in weeks.
        """
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Converts days into weeks.

        Args:
            days (int): The duration of the course in days.

        Returns:
            int: The equivalent duration in weeks.
                 The last week may not be whole.
        """
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        """
        Creates an OnlineCourse instance from a dictionary.

        Args:
            course_dict (dict): A dictionary containing course details.
                - "name" (str): The name of the course.
                - "description" (str): A brief description of the course.
                - "days" (int): The duration of the course in days.

        Returns:
            OnlineCourse: A new OnlineCourse instance with the given details.
        """
        return cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"]),
        )
