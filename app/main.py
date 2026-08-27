class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        """
        Initialize the OnlineCourse instance.

        :param name: Name of the course.
        :param description: Description of the course.
        :param weeks: Duration of the course in weeks.
        """
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Convert course duration from days to weeks.

        :param days: Duration of the course in days.
        :return: Equivalent duration in weeks.
        """
        return (days + 6) // 7  # Adding 6 ensures that partial weeks round up.

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """
        Create an OnlineCourse instance from a dictionary.

        :param course_dict: Dictionary with course information.
        :return: An instance of OnlineCourse.
        """
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name=name, description=description, weeks=weeks)
