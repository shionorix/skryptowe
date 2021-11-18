from typing import List
from term import Term
import lesson
from day import Day
from action import Action

class BasicTimetable(object):
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self.lessons = []
        self.table = {Day.MON: [""]*8, Day.TUE: ['']*8, Day.WED: ['']*8, Day.THU: ['']*8, Day.FRI: ['']*8, Day.SAT: ['']*8, Day.SUN: ['']*8}
        self.hourtrans = {(8,0): 0, (9,30): 1, (11,0): 2, (12,30): 3, (14,0): 4, (15,30): 5, (17,0): 6, (18,30): 7}


    def put(self, lesson: lesson.Lesson) -> bool:
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
        actions_trans = { 
        Action.TIME_EARLIER : lesson.Lesson.earlierTime,
        Action.TIME_LATER : lesson.Lesson.laterTime,
        Action.DAY_LATER : lesson.Lesson.laterDay,
        Action.DAY_EARLIER : lesson.Lesson.earlierDay
        }
        for i in range(len(actions)):
            temp = self.lessons[i%(len(self.lessons))]
            self.table[temp.term.day][self.hourtrans[temp.term.start_time()]] = ''
            actions_trans[actions[i]](temp)
            self.lessons[i%(len(self.lessons))] = temp
            self.table[temp.term.day][self.hourtrans[temp.term.start_time()]] = temp


    def get(self, term: Term) -> lesson.Lesson:
        return self.table[term.day][self.hourtrans[term.start_time()]]
        