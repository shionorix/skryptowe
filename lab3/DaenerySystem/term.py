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
        self.__hour = hour
        self.__minute = minute 
        self.__duration = duration
        self.__day = day

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        if type(value) is not int:
            raise TypeError('Podano niepoprawną wartość godziny.')
        elif value < 8 or value > 20:
            raise ValueError('Podano niepoprawną wartość godziny.')
        else:
            self.__hour = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if type(value) is not int:
            raise TypeError('Podano niepoprawną wartość minut')
        elif value < 0 or value > 59:
            raise ValueError('Podano niepoprawną wartość minut')
        else:
            self.__minute = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if type(value) is not Day:
            raise TypeError('Dzień musi być typu \'Day\'')
        else:
            self.__day = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if type(value) is not int:
            raise TypeError('Niepoprawny czas trwania')
        elif value <=0:
            raise ValueError('Niepoprawny czas trwania')
        else:
            self.__duration = value

    def __sub__(self, other): # - operator
        return Term(other.__hour, other.__minute, duration=self.__hour*60+self.__minute+self.__duration-other.__hour*60-other.__minute)
    
    def __str__(self):
        if self.__day == None:
            return f"{self.__hour}:{self.__minute} [{self.__duration}]"
        return f"{self.trans[self.__day]} {self.__hour}:{self.__minute} [{self.__duration}]"
    
    def __lt__(self, termin): # < operator
        if self.__hour < termin.__hour:
            return True
        elif self.__hour == termin.__hour:
            if self.__minute < termin.__minute:
                return True
        return False

    def __eq__(self, termin): # == operator
        if str(self) == str(termin):
            return True
        return False

    def __le__(self, termin): # <= operator
        if self < termin or self == termin:
            return True
        return False
    
    def __gt__(self, termin): # > operator
        if self.__hour > termin.__hour:
            return True
        elif self.__hour == termin.__hour:
            if self.__minute > termin.__minute:
                return True
        return False
    
    def __ge__(self, termin): # >= operator
        if self > termin or self == termin:
            return True
        return False

    def end_time(self):
        add_hour = self.__duration // 60
        add_min = self.__duration % 60
        end_min = self.__minute + add_min

        if end_min >= 60:
            add_hour += 1
            end_min %= 60

        end_hour = self.__hour + add_hour

        return (end_hour, end_min)

#     def setTerm(self, napis):
#         napis = napis.split(' - ')
#         start = napis[0]
#         end = napis[1]
#         print(napis)
#         self.date(start)

#     def date(self, date):
#         date = date.split(" ")
#         hour = date[-1]
#         date.pop()
#         hour = hour.split(":")
#         print(hour)
#         print(date)
#         date_month = month_trans(date[1])
#         date_day = int(date[0])
#         date_year = int(date[2])
#         print(date_month, date_year, date_day)

# def month_trans(month):
#     return  {
#         'I': 1,
#         'II': 2,
#         'III': 3,
#         'IV': 4,
#         'V': 5,
#         'VI': 6,
#         'VII': 7,
#         'VIII': 8,
#         'IX': 9,
#         'X':10,
#         'XI': 11,
#         'XII': 12
#     }[month]


# if __name__ == '__main__':
    # term = Term(Day.TUE, 9, 45)
    # print(term)
    # term.setTerm('27 X 2021 8:00 - 27 X 2021 8:30')

            