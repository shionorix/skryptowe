from typing import List
from term import Term
from lesson import Lesson
from day import Day
from action import Action

class Timetable1(object):
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self.lessons = list()
        self.table = {Day.MON: [""]*8, Day.TUE: ['']*8, Day.WED: ['']*8, Day.THU: ['']*8, Day.FRI: ['']*8, Day.SAT: ['']*8, Day.SUN: ['']*8}
        self.hourtrans = {(8,0): 0, (9,30): 1, (11,0): 2, (12,30): 3, (14,0): 4, (15,30): 5, (17,0): 6, (18,30): 7}

    def __str__(self):
        slots = ['  8:00-9:30', ' 9:30-11:00', '11:00-12:30', '12:30-14:00', '14:00-15:30', '15:30-17:00', '17:00-18:30', '18:30-20:00']
        out = '            *Poniedziałek*Wtorek     *Środa       *Czwartek    *Piątek       *Sobota  *Niedziela\n            ************************************************************************************\n'
        for j in range(0,8):
            for i in range(0,8):
                if i == 0:
                    out += f'\n{slots[j]} '
                elif self.table[Day(i)][j] != '':
                    out += f'* {self.table[Day(i)][j].name} '
                else:
                    out += '*           '
            out += '\n            ************************************************************************************'
        return out

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if not self.busy(term):
            if full_time:
                if term.day.value < 5 and term.hour >= 8 and term.hour*60+term.minute <= 60*20:
                    return True
                elif term.day.value == 5 and term.hour >= 8 and term.hour*60+term.minute <= 60*17:
                    return True
                else:
                    return False
            elif not full_time:
                if term.day.value > 5 and term.hour >= 8 and term.hour*60+term.minute <= 60*20:
                    return True
                elif term.day.value == 5 and term.hour >= 17 and term.hour*60+term.minute <= 60*20:
                    return True
                else:
                    return False
        else:
            return False

    def busy(self, term: Term) -> bool:
        if self.table[term.day][self.hourtrans[term.start_time()]] != '':
            return True
        else:
            return False

    def put(self, lesson: Lesson) -> bool:
        if not self.busy(lesson.term):
            self.table[lesson.term.day][self.hourtrans[lesson.term.start_time()]] = lesson
            self.lessons.append(lesson)
            return True
        
    def parse(self, actions: List[str]) -> List[Action]:
        trans = {'d-':Action.DAY_EARLIER, 'd+': Action.DAY_LATER, 't-': Action.TIME_EARLIER, 't+':Action.TIME_LATER}
        temp = []
        for i in range(len(actions)):
            if actions[i] in trans:
                temp.append(actions[i])

        actions = []
        for i in range(len(temp)):
            actions.append(trans[temp[i]])

        return actions
    

    def perform(self, actions: List[Action]):

        pass

    def get(self, term: Term) -> Lesson:
        return self.table[term.day[self.hourtrans[term.start_time()]]]
        
if __name__ == '__main__':
    tab = ['d+', 'd-','hygyh', 't+', 't-']
    t = Timetable1()
    tab = Timetable1.parse(t, tab)
    lesson1 = Lesson(Term(8, 0, 90, Day.FRI), "Angielski", "", 2)
    lesson2 = Lesson(Term(18, 30, 90, Day.WED), "Programowanie", "Stanisław Polak", 2)
    t.put(lesson1)
    t.put(lesson2)
    print(t)
   # print(tab)