class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        # Ceiling division by 7: converts days to weeks, counting any remainder as a full week
        return (days + 6) // 7

    @classmethod
    def from_dict(cls, course_dict):
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"]),
        )
