from types import NoneType
from day import Day
from term import Term
from teacher import Teacher

class Lesson(object):
    def __init__(self, term: Term, name: str, teacherName: str, year: int, timetable = None):
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__timetable = timetable
        self.__teacher = None

        if term.day.value < 5:
            if term.hour*60+term.minute+term.duration <= 20*60 and term.hour >= 8:
                self.__full_time = True
            else:
                self.__full_time = None
        elif term.day.value == 5:
            if term.hour*60+term.minute+term.duration <= 17*60 and term.hour >= 8:
                self.__full_time = True
            elif term.hour*60+term.minute+term.duration <= 20*60 and term.hour >= 17:
                self.__full_time = False
            else:
                self.__full_time = None
        else:
            if term.hour*60+term.minute+term.duration <= 20*60 and term.hour >= 8:
                self.__full_time = False
            else:
                self.__full_time = None

        self.trans = {
            1: "Pierwszy rok",
            2: "Drugi rok",
            3: "Trzeci rok",
            4: "Czwarty rok",
            5: "Piąty rok",
            True: "studia stacjonarne",
            False: "studia niestacjonarne",
        }

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if type(value) is Teacher or type(value) is NoneType:
            self.__teacher = value
        else:
            raise TypeError('Pole teacher musi być typu Teacher lub NoneType')

    def __add__(self, newteacher):
        if type(newteacher) is Teacher:
            temp = newteacher.workduration + self.term.duration
            if temp <= 6*45:
                newteacher.workduration = temp
                self.teacher = newteacher
        return self.teacher

    def __sub__(self, teacher):
        if type(teacher) is Teacher:
            if teacher == self.teacher:
                teacher.workduration -= self.term.duration
                self.teacher = None
        return self.teacher

    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def timetable(self, value):
        import timetable1
        if type(value) is not timetable1.Timetable1:
            raise TypeError('Plan zajęc musi być typu \'Timetable1\'')
        else:
            self.__timetable = value

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        if type(value) is not Term:
            raise TypeError('Termin musi być typu \'Term\'')
        else:
            self.__term = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('Nazwa przedmiotu musi być typu \'str\'')
        else:
            self.__term = value

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, value):
        if type(value) is not str:
            raise TypeError('Nazwisko prowadzącego musi być typu \'str\'')
        else:
            self.__teacherName = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if type(value) is not int:
            raise TypeError('Niepoprawna wartość roku')
        elif value <= 0:
            raise ValueError('Niepoprawna wartość roku')
        else:
            self.__year = value

    @property
    def full_time(self):
        return self.__full_time

    def __str__(self):
        return f"{self.name} ({self.term})\n{self.trans[self.year]}, {self.trans[self.full_time]}\nProwadzący: {self.teacherName}"

    def earlierDay(self):
        if self.term._Term__day.value-1 > 0 and self.full_time == Lesson(Term(self.term.hour,self.term.minute,self.term.duration,Day(self.term._Term__day.value-1)), self.name, self.teacherName,self.year).full_time:
            self.term._Term__day = Day(self.term._Term__day.value-1)

    def laterDay(self):
        if self.term._Term__day.value+1 < 8 and self.full_time == Lesson(Term(self.term.hour,self.term.minute,self.term.duration,Day(self.term._Term__day.value+1)), self.name, self.teacherName,self.year).full_time:
            self.term._Term__day = Day(self.term._Term__day.value+1)

    def earlierTime(self):
        t = self.term.duration%60
        if self.term.minute >= t:
            if self.full_time == Lesson(Term(self.term.hour-(self.term.duration//60),self.term.minute-t,self.term.duration,Day(self.term._Term__day.value)), self.name, self.teacherName,self.year).full_time:
                self.term.hour -= self.term.duration//60
                self.term.minute -= t
        else:
            if self.full_time == Lesson(Term(self.term.hour-(self.term.duration//60),self.term.minute-(t-60),self.term.duration,Day(self.term._Term__day.value)), self.name, self.teacherName,self.year).full_time:
                self.term.hour -= 1
                self.term.minute -= (t-60)

    def laterTime(self):
        t = self.term.duration%60
        if self.term.minute + t <= 60:
            if self.full_time == Lesson(Term(self.term.hour+(self.term.duration//60),self.term.minute+t,self.term.duration,Day(self.term._Term__day.value)), self.name, self.teacherName,self.year).full_time:
                self.term.hour += self.term.duration//60
                self.term.minute += t
        else:
            if self.full_time == Lesson(Term(self.term.hour+(self.term.duration//60)+1,self.term.minute+(t-60),self.term.duration,Day(self.term._Term__day.value)), self.name, self.teacherName,self.year).full_time:
                self.term.hour += (self.term.duration//60)+1
                self.term.minute += (t-60)

