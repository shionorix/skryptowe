from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7
    def difference(self, day):
        d = day.value - self.value
        if d > 3:
            return d - 7
        elif d < -3:
            return d + 7
        else:
            return d

def nthDayFrom(n, day):
    res = Day((n - 1 + day.value) % 7 + 1)
    return res