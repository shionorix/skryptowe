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
        if d > 4:
            return d - 7
        elif d < -4:
            return d + 7
        else:
            return d

    def __str__(self):
        str_val = {
            1: 'Poniedziałek',
            2: 'Wtorek',
            3: 'Środa',
            4: 'Czwartek',
            5: 'Piątek',
            6: 'Sobota',
            7: 'Niedziela'
        }
        return str_val[self.value]

def nthDayFrom(n, day):
    res = Day((n - 1 + day.value) % 7 + 1)
    return res