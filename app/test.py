import math

def days_to_weeks(days) -> int:
    return math.ceil(days / 7)


print(days_to_weeks(15))