#%%
class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        weeks = -(-days//7)
        return weeks
    
    @classmethod
    def from_dict(cls, course_dict):
        weeks = cls.days_to_weeks(course_dict['days'])
        return cls(name=course_dict['name'],description=course_dict['description'],weeks=weeks)

#%%
course = OnlineCourse(name = "python", description="proba", weeks=2)
# %%
course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
# %%
course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)
# %%
python_course = OnlineCourse.from_dict(course_dict)
# %%
python_course.weeks