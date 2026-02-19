from typing import Self
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        weeks = math.ceil(data["days"] / 7)
        return cls(
            name=data["name"],
            description=data["description"],
            weeks=weeks
        )
