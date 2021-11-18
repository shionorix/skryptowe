from typing import List
from term import Term
import lesson
from action import Action

class BasicTimetable(object):
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self.lessons = {}

    def put(self, less: lesson.Lesson) -> bool:
        if type(less) is not lesson.Lesson:
            raise TypeError('Nieprawidłowy typ danych')
        else:
            for i in list(self.lessons.values()):
                if i.term == less.term:
                    raise ValueError('Zajęty termin')
            self.lessons[f'{less.term.start_time()} - {less.term.end_time()}'] = less
            return True
    
    def parse(self, actions: List[str]) -> List[Action]:
        trans = {'d-':Action.DAY_EARLIER, 'd+': Action.DAY_LATER, 't-': Action.TIME_EARLIER, 't+':Action.TIME_LATER}
        temp = []
        for i in range(len(actions)):
            if actions[i] in trans:
                temp.append(actions[i])
            else:
                raise ValueError('Translation incorrect')

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
        index = 0
        for i in range(len(actions)):
            temp = list(self.lessons.values())[index]
            old_term = list(self.lessons.keys())[index]
            actions_trans[actions[i]](temp)
            new_term = f'{temp.term.start_time()} - {temp.term.end_time()}'
            self.lessons[new_term] = self.lessons.pop(old_term)
            index %= len(list(self.lessons.values()))

    def get(self, term: Term) -> lesson.Lesson:
        if f'{term.start_time()} - {term.end_time()}' in list(self.lessons):
            return self.lessons[f'{term.start_time()} - {term.end_time()}']
        else:
            raise ValueError('Nie ma lekcji o podanym terminie')
        