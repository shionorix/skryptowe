from day import Day
import basicterm

class Term(basicterm.BasicTerm):
    def __init__(self, hour, minute, duration, day: Day):
        super().__init__(hour, minute, duration)
        self.__day = day

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if type(value) is not Day:
            raise TypeError('Dzień musi być typu \'Day\'')
        else:
            self.__day = value
    
    def __str__(self):
        if self.day == None:
            return f"{self.hour}:{self.minute} [{self.duration}]"
        return f"{str(self.day)} {self.hour}:{self.minute} [{self.duration}]"
    
