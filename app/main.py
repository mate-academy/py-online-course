from __future__ import annotations
import math


class OnlineCourse:
    """A class to represent an online course.

    :param name: The name of the course.
    :type name: str
    :param description: The description of the course.
    :type description: str
    :param weeks: The duration of the course in weeks.
    :type weeks: int
    """

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """Converts days to weeks.

        :param days: The number of days.
        :type days: int
        :return: The number of weeks.
        :rtype: int
        """
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        """Creates an OnlineCourse object from a dictionary.

        :param course_dict: A dictionary containing course information.
        :type course_dict: dict
        :return: An OnlineCourse object.
        :rtype: OnlineCourse
        """
        return cls(
            course_dict["name"],
            course_dict["description"],
            cls.days_to_weeks(course_dict["days"])
        )

    def __init__(
        self,
        name: str,
        description: str,
        weeks: int
    ) -> None:
        """Initializes an OnlineCourse object.

        :param name: The name of the course.
        :type name: str
        :param description: The description of the course.
        :type description: str
        :param weeks: The duration of the course in weeks.
        :type weeks: int
        """
        self.name = name
        self.description = description
        self.weeks = weeks
