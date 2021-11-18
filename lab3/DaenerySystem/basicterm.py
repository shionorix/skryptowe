class BasicTerm(object):
    def __init__(self, hour: int, minute: int, duration: int):
        self.__hour = hour
        self.__minute = minute 
        self.__duration = duration

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
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if type(value) is not int:
            raise TypeError('Niepoprawny czas trwania')
        elif value <= 0:
            raise ValueError('Niepoprawny czas trwania')
        else:
            self.__duration = value

    def __sub__(self, other): # - operator
        return BasicTerm(other.hour, other.minute, duration=self.hour*60+self.minute+self.duration-other.hour*60-other.minute)
    
    def __lt__(self, termin): # < operator
        if self.hour < termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute < termin.minute:
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
        if self.hour > termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute > termin.minute:
                return True
        return False
    
    def __ge__(self, termin): # >= operator
        if self > termin or self == termin:
            return True
        return False

    def start_time(self):
        return (self.hour, self.minute)
        
    def end_time(self):
        add_hour = self.duration // 60
        add_min = self.duration % 60
        end_min = self.minute + add_min

        if end_min >= 60:
            add_hour += 1
            end_min %= 60

        end_hour = self.hour + add_hour

        return (end_hour, end_min)