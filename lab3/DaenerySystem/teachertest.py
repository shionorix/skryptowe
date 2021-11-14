import unittest
from teacher import Teacher
from lesson import Lesson
from timetable1 import Timetable1
from term import Term
from day import Day

class Test_teacher(unittest.TestCase):
    teacher = Teacher('Stanisław', 'Polak')
    tt = Timetable1()
    lesson1 = Lesson(Term(8, 0, 90, Day.FRI), "lekcja1", "-", 2, tt)        
    lesson2 = Lesson(Term(18, 30, 90, Day.WED), "lekcja2", "-", 2, tt)
    lesson3 = Lesson(Term(8, 0, 90, Day.SAT), "lekcja3", "-", 2, tt)
    lesson4 = Lesson(Term(8, 0, 90, Day.WED), "lekcja4", "-", 2, tt)
    tt.put(lesson1)
    tt.put(lesson2)
    tt.put(lesson3)
    tt.put(lesson4)

    def test_str(self):
        self.assertEqual(str(self.teacher), 'Stanisław Polak')

    def test_add(self):
        self.assertEqual(self.lesson1 + self.teacher, self.teacher)
        self.assertEqual(self.lesson2 + self.teacher, self.teacher)
        self.assertEqual(self.lesson3 + self.teacher, self.teacher)
        self.assertEqual(self.lesson4 + self.teacher, None)

    def test_sub(self):
        self.assertEqual(self.lesson1 - self.teacher, None)
        self.assertEqual(self.lesson4 - self.teacher, None)


if __name__ == '__main__':
    unittest.main()