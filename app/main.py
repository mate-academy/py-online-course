from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    def days_to_weeks(self: int) -> int:
        weeks = ceil(self / 7)
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> object:
        new_dict = {}
        for key, value in course_dict.items():
            if key == "days":
                new_dict["weeks"] = OnlineCourse.days_to_weeks(value)
            elif key != "days":
                new_dict[key] = value
        return cls(new_dict["name"],
                   new_dict["description"],
                   new_dict["weeks"])
