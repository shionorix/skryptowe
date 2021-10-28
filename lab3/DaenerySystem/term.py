from day import Day

class Term(object):
    def __init__(self, day, hour, minute, duration = 90):
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

    def __str__(self):
        if self.__day == None:
            return f"{self.hour}:{self.minute} [{self.duration}]"
        return f"{self.trans[self.__day]} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin):
        if termin.hour < self.hour:
            return False
        elif termin.hour == self.hour:
            if termin.minute < self.minute:
                return False
        else:
            return True
            
    def laterThan(self, termin):
        if termin.hour > self.hour:
            return False
        elif termin.hour == self.hour:
            if termin.minute > self.minute:
                return False
        else:
            return True

    def equals(self, termin):
        if termin.hour == self.hour and termin.minute == self.minute and termin.duration == self.duration:
            return True
        else:
            return False

            