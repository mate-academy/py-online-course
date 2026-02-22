class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(weeks: int) -> int:
        """
        Converts number of days to weeks. rounded up
        :param weeks: takes number of days
        :return: weeks rounded up
        """
        return (weeks + 6) // 7

    @classmethod
    def from_dict(cls, course_dict: dict[str | int]) -> "OnlineCourse":
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=cls.days_to_weeks(course_dict["days"])
                   )
