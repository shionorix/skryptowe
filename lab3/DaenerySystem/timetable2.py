import bre4k
from term import Term
import lesson
from day import Day
from action import Action
import basictimetable

class Timetable2(basictimetable.BasicTimetable):
    skipBreaks = True

    def __init__(self, breaks: list[bre4k.Break]):
        super(Timetable2, self).__init__()
        self.__breaks = breaks

    @property
    def breaks(self):
        return self.__breaks

    @breaks.setter
    def breaks(self, value):
        if type(value) is not list[bre4k.Break]:
            raise TypeError('Nieprawidłowy typ listy przerw')
        else:
            self.__breaks = value

    def __str__(self):
        terms = []
        display = []
        starthours = []

        for less in list(self.lessons.values()): # lista terminów  których odbywają się lekcje
            terms.append(less.term)
            starthours.append(less.term.start_time())

        for bre in self.breaks: # dodanie terminów przerw
            terms.append(bre)
            starthours.append(bre.start_time())
        starthours.sort()
        terms = sorted(terms, key=lambda t: t.start_time())
        for i in range(8): # pola na lekcje i przerwy
            display.append([])
            for j in range(len(terms) + 1):
                display[i].append('')
        
        for d in Day: # linia z dniami
            display[d.value][0] = str(d)

        for position, term in enumerate(terms): # kolumna z godzinami
            display[0][position + 1] = f'{":".join(map(str, term.start_time()))}-{":".join(map(str, term.end_time()))}'

        for less in list(self.lessons.values()): # wpisanie lekcji w odpowiednie pola
            display[less.term.day.value][terms.index(less.term) + 1] = less.name
        
        for bre in self.breaks: # wpisanie przerw w odpowiednie pola
            for day in range(1,8):
                display[day][starthours.index(bre.start_time()) + 1] = '-----'
        
        separator = f'\n{"": ^12}{"":*^92}\n'
        output = ''
        for i in range(len(terms) + 1): # formatowanie finalnego wypisania planu lekcji
            for j in range(8):
                output += f'{display[j][i]: ^12}*'
            output += separator
        return output

    def can_be_transfered_to(self, term: Term, full_time: bool) -> bool:
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
            

    def busy(self, term: Term) -> bool: #wrzucenie lekcji i przerw w jedna liste terminów i sprawdzanie ich po kolei czy nie nachodzą, potem w lesson edytować funkcje żeby przesuwały o przerwy
        for lesson in list(self.lessons.values()):
            if lesson.term == term:
                return True
            elif lesson.term.end_time() > term.start_time() and lesson.term.end_time() < term.end_time():
                return True
            elif term.end_time() > lesson.term.start_time() and term.end_time() < lesson.term.end_time():
                return True
            elif lesson.term.start_time() > term.start_time() and lesson.term.start_time() < term.end_time():
                return True
            elif term.start_time() > lesson.term.start_time() and term.start_time() < lesson.term.end_time():
                return True
            else:
                return False

    def breaks_check(self, term: Term): # zwraca przerwe która nachodzi (o ile nachodzi)
        for bre in self.breaks:
            if bre.start_time() < term.start_time() and bre.end_time() > term.start_time():
                return bre
            elif bre.start_time() < term.end_time() and term.end_time() > bre.end_time():
                return bre
            elif bre.start_time() == term.start_time() and bre.end_time() < term.end_time():
                return bre
            elif bre.start_time() > term.start_time() and bre.end_time() == term.end_time():
                return bre
            else:
                return None


if __name__ == '__main__':
    tab = ['d+', 'd-','hygyh', 't+', 't-']
    breaks = [bre4k.Break(9,30,5), bre4k.Break(11,5,10), bre4k.Break(12, 45, 5)]    
    t = Timetable2(breaks)
    lesson1 = lesson.Lesson(Term(8, 0, 90, Day.FRI), "Angielski", "", 2, t)        
    lesson2 = lesson.Lesson(Term(18, 30, 90, Day.WED), "Programowanie", "Stanisław Polak", 2, t)
    t.put(lesson1)
    t.put(lesson2)
    print(t) 
    print(t.get(Term(18, 30, 90, Day.WED)))
    t.perform([Action.DAY_EARLIER,  Action.DAY_LATER,  Action.TIME_LATER,Action.TIME_EARLIER])
    print(t) 
    print(t.lessons)
