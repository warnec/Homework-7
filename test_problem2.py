import unittest
from problem2 import testLeap


class TestCase(unittest.TestCase):

    def test_leap(self):
        self.assertEqual(testLeap(4),"The entered year is a leap year")
    def test_leap(self):
        self.assertEqual(testLeap(400),"The entered year is a leap year")

if __name__ == '__main__':
    unittest.main(verbosity=2)