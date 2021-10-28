from term import Term
from day import Day
import unittest

class Test_Term(unittest.TestCase):
    term2 = Term(Day.WED, 10, 15)
    term1 = Term(Day.TUE, 9, 45)
    def test_str(self):
        print(self.term1, self.term2)

    def test_earlierThan(self):
        self.assertEqual(self.term1.earlierThan(self.term2), True)

    def test_laterThan(self):
        self.assertEqual(self.term1.laterThan(self.term2), False)

    def test_equal(self):
        self.assertEqual(self.term1.equals(self.term2), False)

if __name__ == '__main__':
    unittest.main()