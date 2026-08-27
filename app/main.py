import math


class OnlineCourse:
    """
    Represents an online course with its name, description,
    and duration in weeks.

    This class provides functionality to define and manage
    online courses, including tools to calculate weeks from
    days and create course instances from dictionary data.

    """
    def __init__(self, name: str, description: str, weeks: int) -> None:
        """
        Represents a project with a name, description,
        and duration in weeks.

        The class provides essential attributes to define
        a project including its name, a descriptive text,
        and the duration in weeks.

        :param name: Name of the project.
        :type name: str
        :param description: A brief description of the project.
        :type description: str
        :param weeks: Duration of the project in weeks.
        :type weeks: int
        """
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Converts a given number of days into weeks.

        This method calculates the equivalent number
        of weeks for the given number of days by dividing
        the days by 7 and rounding up to the next
        whole number.

        :param days: The number of days as an integer.
        :type days: int
        :return: The number of weeks obtained from the
            conversion.
        :rtype: int
        """
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """
        Creates an instance of the class based on a
        dictionary input.

        This class method is responsible for constructing
        an instance of the class by extracting relevant
        information from the provided dictionary.
        The method internally converts the "days" from
        the dictionary to "weeks" by calling the
        `days_to_weeks` class method.

        :param course_dict: A dictionary containing course
            details with the keys  "name" for course name,
            "description" for course description, and
            "days" indicating the duration of the course
            in days.
        :type course_dict: dict

        :return: An instance of the class initialized
            with the provided course details.
        :rtype: OnlineCourse
        """
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=weeks
        )
