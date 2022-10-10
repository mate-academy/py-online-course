class OnlineCourse:
    def __int__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, ):
        ...

    def course_dict(self, ):
        ...

    @staticmethod
    def days_to_weeks(days):
        result = int(days / 7 + 1) if isinstance(days / 7, float) else days / 7
        return result
