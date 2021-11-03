from day import Day 
from term import Term
from lesson import Lesson
import unittest

class test_lesson(unittest.TestCase):
    lesson1 = Lesson(Term(8, 0, 90, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
    lesson2 = Lesson(Term(17, 50, 90, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)

    def test_earlierDay(self):
        self.lesson1.earlierDay()
        self.assertEqual(self.lesson1.term._Term__day, Day.THU)
        self.lesson2.earlierDay()
        self.assertEqual(self.lesson2.term._Term__day, Day.MON)

    def test_laterDay(self):
        self.lesson1.laterDay()
        self.assertEqual(self.lesson1.term._Term__day, Day.FRI)
        self.lesson1.laterDay()
        self.assertEqual(self.lesson1.term._Term__day, Day.FRI)

    def test_earlierTime(self):
        self.lesson1.earlierTime()
        self.assertEqual(self.lesson1.term.hour, 8)
        self.assertEqual(self.lesson1.term.minute, 0)
        self.lesson2.earlierTime()
        self.assertEqual(self.lesson2.term.hour, 16)
        self.assertEqual(self.lesson2.term.minute, 20)

    def test_laterTime(self):
        self.lesson2.laterTime()
        self.assertEqual(self.lesson2.term.hour, 17)
        self.assertEqual(self.lesson2.term.minute, 50)
        self.lesson2.laterTime()
        self.assertEqual(self.lesson2.term.hour, 17)
        self.assertEqual(self.lesson2.term.minute, 50)


if __name__ =='__main__':
    unittest.main()