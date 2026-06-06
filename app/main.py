class OnlineCourse:
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        result = days // 7
        if days % 7 > 0:
            result += 1
        return result

    def from_dict(self):
