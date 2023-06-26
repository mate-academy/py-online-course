class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
    
    @staticmethod
    def days_to_weeks(days: int) -> int:
        other = days % 7
        weeks = days // 7
        if other:
            return weeks + 1
        return weeks