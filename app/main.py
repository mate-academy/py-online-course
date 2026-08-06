class OnlineCourse:

    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    def days_to_weeks(self):
        ost = self % 7
        wek = int(self / 7)
        if ost != 0:
            return wek + 1
        else:
            return wek

    @classmethod
    def from_dict(cls, course_dict):
        return cls(
            course_dict['name'],
            course_dict['description'],
            OnlineCourse.days_to_weeks(course_dict['days'])
        )
