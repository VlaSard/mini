import unittest
from day_in_month import *


class TestDayInMonth(unittest.TestCase):

    def test_days(self):
        self.assertEqual(day_in_month(2, 2022), (28, False))
        self.assertEqual(day_in_month(2, 2024), (29, True))

    def test_values(self):
        self.assertRaises(ValueError, day_in_month, -1, 2022)
        self.assertRaises(ValueError, day_in_month, 0, -2024)

    def test_types(self):
        self.assertRaises(TypeError, day_in_month, '2a', 2022)
        self.assertRaises(TypeError, day_in_month, 5, "may")
        self.assertRaises(TypeError, day_in_month, [True, False], [False, True])
