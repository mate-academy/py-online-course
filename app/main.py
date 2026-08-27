class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        """
        Initialize a new OnlineCourse object.

        Args:
            name (str): The name of the course.
            description (str): The description of the course.
            weeks (int): The duration of the course in weeks.
        """
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        """
        Convert days to weeks. The last week may not be whole.

        Args:
            days (int): Number of days.

        Returns:
            int: Number of weeks.
        """
        # If the days divide evenly by 7, return that number of weeks
        # Otherwise, add an extra week for the remaining days
        if days % 7 == 0:
            return days // 7
        else:
            return days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        """
        Create a new OnlineCourse instance from a dictionary.

        Args:
            course_dict (dict): Dictionary containing course information with
                keys 'name', 'description', and 'days'.

        Returns:
            OnlineCourse: A new instance of the OnlineCourse class.
        """
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]

        # Convert days to weeks
        weeks = cls.days_to_weeks(days)

        # Create and return a new OnlineCourse instance
        return cls(name=name, description=description, weeks=weeks)
