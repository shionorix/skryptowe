from day import Day
from term import Term

class Lesson(object):
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        if term._Term__day.value < 5:
            if term.hour*60+term.minute+term.duration <= 20*60 and term.hour*60+term.minute >= 8*60:
                self.full_time = True
            else:
                self.full_time = None
        elif term._Term__day.value == 5:
            if term.hour*60+term.minute+term.duration <= 17*60 and term.hour*60+term.minute >= 8*60:
                self.full_time = True
            elif term.hour*60+term.minute+term.duration <= 20*60 and term.hour*60+term.minute >= 17*20:
                self.full_time = False
            else:
                self.full_time = None
        else:
            if term.hour*60+term.minute+term.duration <= 20*60 and term.hour*60+term.minute >= 8*60:
                self.full_time = False
            else:
                self.full_time = None

        self.trans = {
            1: "Pierwszy rok",
            2: "Drugi rok",
            3: "Trzeci rok",
            4: "Czwarty rok",
            5: "Piąty rok",
            True: "studia stacjonarne",
            False: "studia niestacjonarne",
        }

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
                self.term.hour-=self.term.duration//60
                self.term.minute -= t
        else:
            if self.full_time == Lesson(Term(self.term.hour-(self.term.duration//60),self.term.minute-(t-60),self.term.duration,Day(self.term._Term__day.value)), self.name, self.teacherName,self.year).full_time:
                self.term.hour -= 1
                self.term.minute -= (t-60)

    def laterTime(self):
        t = self.term.duration%60
        if self.term.minute + t <= 60:
            if self.full_time == Lesson(Term(self.term.hour+(self.term.duration//60),self.term.minute+t,self.term.duration,Day(self.term._Term__day.value)), self.name, self.teacherName,self.year).full_time:
                self.term.hour+=self.term.duration//60
                self.term.minute += t
        else:
            if self.full_time == Lesson(Term(self.term.hour+(self.term.duration//60)+1,self.term.minute+(t-60),self.term.duration,Day(self.term._Term__day.value)), self.name, self.teacherName,self.year).full_time:
                self.term.hour += (self.term.duration//60)+1
                self.term.minute += (t-60)


if __name__ == '__main__':
    lesson = Lesson(Term(8, 35, 90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
    print(lesson); 
    lesson.earlierDay()
    print(lesson)
    lesson.laterDay()
    print(lesson)
    lesson.earlierTime()
    print(lesson)
    lesson.laterTime()
    print(lesson)