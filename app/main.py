class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int):
        if days <= 7:
            return 1
        if days > 7 and days % 7 != 0:
            weeks = days // 7 + 1
        else:
            weeks = days / 7
        return int(weeks)

    @classmethod
    def from_dict(cls, course_dict: dict):
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        return cls(name=name,
                   description=description,
                   weeks=cls.days_to_weeks(days))


course = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12}

python_course = OnlineCourse.from_dict(course)
print(python_course.__dict__)
print(python_course.name)
print(python_course.description)
print(python_course.weeks)
