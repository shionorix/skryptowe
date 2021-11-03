from day import Day

class Term(object):
    def __init__(self, hour, minute, duration = 90, day = None):
        self.trans ={
            Day.MON: "Poniedzialek",
            Day.TUE: "Wtorek",
            Day.WED: "Środa",
            Day.THU: "Czwartek",
            Day.FRI: "Piątek",
            Day.SAT: "Sobota",
            Day.SUN: "Niedziela"
        }
        self.hour = hour
        self.minute = minute 
        self.duration = duration
        self.__day = day


    def __sub__(self, other):
        return Term(other.hour, other.minute, duration=self.hour*60+self.minute+self.duration-other.hour*60-other.minute)
    
    def __str__(self):
        if self.__day == None:
            return f"{self.hour}:{self.minute} [{self.duration}]"
        return f"{self.trans[self.__day]} {self.hour}:{self.minute} [{self.duration}]"
    
    def __lt__(self, termin):
        if self.hour < termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute < termin.minute:
                return True
        return False

    def __eq__(self, termin):
        if str(self) == str(termin):
            return True
        return False

    def __le__(self, termin):
        if self < termin or self == termin:
            return True
        return False
    
    def __gt__(self, termin):
        if self.hour > termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute > termin.minute:
                return True
        return False
    
    def __ge__(self, termin):
        if self > termin or self == termin:
            return True
        return False

    def setTerm(self, napis):
        napis = napis.split(' - ')
        start = napis[0]
        end = napis[1]
        print(napis)
        self.date(start)

    def date(self, date):
        date = date.split(" ")
        hour = date[-1]
        date.pop()
        hour = hour.split(":")
        print(hour)
        print(date)
        date_month = month_trans(date[1])
        date_day = int(date[0])
        date_year = int(date[2])
        print(date_month, date_year, date_day)

def month_trans(month):
    return  {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,
        'X':10,
        'XI': 11,
        'XII': 12
    }[month]


# if __name__ == '__main__':
    # term = Term(Day.TUE, 9, 45)
    # print(term)
    # term.setTerm('27 X 2021 8:00 - 27 X 2021 8:30')

            