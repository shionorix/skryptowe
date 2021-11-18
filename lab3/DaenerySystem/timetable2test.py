import unittest
import lesson
import timetable2
import term
import day
import bre4k
from action import Action

class Test_timetable2(unittest.TestCase):
    breaks = [bre4k.Break(9,30,5), bre4k.Break(11,5,10), bre4k.Break(12, 45, 5), bre4k.Break(14, 20, 20), bre4k.Break(16, 10, 5)]    

    def test_breaks(self):
        self.assertEqual(str(bre4k.Break(9,30,5)), 'Przerwa')
        self.assertEqual(bre4k.Break(9,30,5).getTerm(), "(9, 30) - (9, 35)")
    
    def test_breaks_true(self):
        t = timetable2.Timetable2(self.breaks)
        lesson1 = lesson.Lesson(term.Term(11, 15, 90, day.Day.WED), "Angielski", "", 2, t)        
        lesson2 = lesson.Lesson(term.Term(9, 35, 90, day.Day.FRI), "Programowanie", "", 2, t)
        actions = [Action.TIME_LATER,Action.TIME_EARLIER]
        t.put(lesson1)
        t.put(lesson2)
        t.perform(actions)
        self.assertEqual(lesson1.term.start_time(), (12, 50))
        self.assertEqual(lesson2.term.start_time(), (8, 0))

    def test_breaks_false(self):
        t2 = timetable2.Timetable2(self.breaks)
        t2.skipBreaks = False
        lesson3 = lesson.Lesson(term.Term(11, 15, 90, day.Day.WED), "Angielski", "", 2, t2)        
        lesson4 = lesson.Lesson(term.Term(9, 35, 90, day.Day.FRI), "Programowanie", "", 2, t2)
        actions = [Action.TIME_LATER, Action.TIME_EARLIER]
        t2.put(lesson3)
        t2.put(lesson4)      
        t2.perform(actions)   
        self.assertEqual(lesson3.term.start_time(), (12, 45))
        self.assertEqual(lesson4.term.start_time(), (8, 5))

    def test_errors(self):
        t2 = timetable2.Timetable2(self.breaks)
        with self.assertRaises(ValueError):
            t2.parse(['jhfdwuj'])
        with self.assertRaises(TypeError):
            t2.put(['jhfdwuj'])
        with self.assertRaises(ValueError):
            t2.put(lesson.Lesson(term.Term(11, 15, 90, day.Day.WED), "Angielski", "", 2, t2))
            t2.put(lesson.Lesson(term.Term(11, 15, 90, day.Day.WED), "Angielski", "", 2, t2))
        with self.assertRaises(ValueError):
            t2.get(term.Term(12, 15, 90, day.Day.WED))

if __name__ == '__main__':
    unittest.main()
