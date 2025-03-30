class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        if days % 7 != 0:
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict):
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = cls.days_to_weeks(course_dict["days"])
        return cls(name=name, description=description, weeks=weeks)

# course = OnlineCourse(
#     name="Python Basics",
#     description="The best course to start learning Python",
#     weeks=2,
# )
# print(course.description)  # The best course to start learn Python
# Often we will receive information about the course in the form of a course_dict dictionary with such fields:
#
# course_dict["name"] - course name
# course_dict["description"] - course description
# course_dict["days"] - duration of the course in days
# To convert course duration to weeks, OnlineCourse should have days_to_weeks staticmethod, that takes one argument days and convert this number to weeks.
#
# Note: The last week may not be whole.
#
# Example:
#
# OnlineCourse.days_to_weeks(10) == 2
# OnlineCourse.days_to_weeks(14) == 2
# OnlineCourse.days_to_weeks(15) == 3
# OnlineCourse should have from_dict classmethod. It should take two parameters:
#
# cls - a default parameter for classmethod
# course_dict - a dictionary described above
# Method should return a new instance of OnlineCourse with correct attributes. It should use days_to_weeks method to convert days to weeks. Example:
#
# course_dict = {
#     "name": "Python Core",
#     "description": "After this course you will know everything about Python",
#     "days": 12,
# }
# python_course = OnlineCourse.from_dict(course_dict)
# print(python_course.weeks)  # 2